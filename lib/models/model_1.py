#create
#list all
#update objects
#delete
#constructor
#find by id
#view related objects
from models.__init__ import CURSOR, CONN;
from models.mycol import MyCol;
class MyBase:
    def __init__(self, tablename = "", cols = None):
        #an array of colobjs
        #column name, type, ispkey, isfkey
        self.setTableName(tablename);
        self.setCols(cols);
    
    def getTableName(self):
        if (type(self._tablename) == str and 0 < len(self._tablename)):
            return self._tablename;
        else: raise Exception("tablename must not be an empty string!");

    def setTableName(self, val):
        if (type(val) == str): self._tablename = val;
        else: raise Exception("tablename must be a string!");

    tablename = property(getTableName, setTableName);

    def setCols(self, val):
        if (val == None or len(val) < 1):
            if (self._cols == None): pass;
            else: self._cols.clear();
            self._cols = val;
        else:
            for item in val:
                if (isinstance(item, MyCol)): pass;
                else: raise Exception("the item must be of type MyCol, but it was not!");
        self._cols = val;
    
    def getCols(self): return self._cols;

    cols = property(getCols, setCols);

    def valMustBeBool(self, val, varname = "var"):
        if (type(varname) == str and 0 < len(varname)): pass;
        else: raise Exception("varname must be a string with at least one character!");
        if (val == True or val == False): return True;
        else: raise Exception("" + varname + " must be a boolean value, but it was not");

    def getColListAsString(self, usefull, noid = False, useaddstronly = False, addstr = ""):
        self.valMustBeBool(usefull, "usefull");
        self.valMustBeBool(noid, "noid");
        self.valMustBeBool(useaddstronly, "useaddstronly");
        if (type(addstr) == str): pass;
        else: raise Exception("addstring must be a string!");
        mystr = "(";
        for n in range(len(self.cols)):
            skipcol = False;
            if (usefull): mystr += self.cols[n].__repr__();
            else:
                clnmstr = "" + self.cols[n].getColName();
                if (noid):
                    if (clnmstr == "id"): skipcol = True;
                    else: skipcol = False;
                if (skipcol): pass;
                else:
                    if (useaddstronly): mystr += "" + addstr;
                    else: mystr += "" + clnmstr + "" + addstr;
            if ((n + 1 < len(self.cols)) and (usefull or not skipcol)): mystr += ", ";
        return mystr + ")";

    def getNameEqualsColList(self):
        mystr = self.getColListAsString(False, True, False, " = ?");
        #usefull False, noid True, useaddstronly False, addstr " = ?"
        return mystr[1:-1];#remove the () surrounding it

    def replaceQuestionsForValues(self, noid = True):
        #usefull False, noid True, useaddstronly True, addstr " = ?"
        return "" + self.getColListAsString(False, noid, True, "?");

    def genSQLCommand(self, commandtypestr, noidoninsert = True):
        self.valMustBeBool(noidoninsert, "noidoninsert");
        basecmdstr = "" + commandtypestr + " " + self.getTableName();
        print(f"basecmdstr = {basecmdstr}");
        if (commandtypestr == "CREATE TABLE"):
            return "" + basecmdstr + " " + self.getColListAsString(True);
        elif (commandtypestr == "DELETE FROM"):
            print(basecmdstr + " WHERE ");
            return "" + basecmdstr + " WHERE "; 
        elif (commandtypestr == "DROP TABLE"):
            print(basecmdstr);
            return "" + basecmdstr;
        elif (commandtypestr == "INSERT INTO"):
            mystr = "" + basecmdstr + " ";
            if (noidoninsert): mystr += self.getColListAsString(False, True, False, "");
            else: mystr += self.getColListAsString(False, False, False, "");
            mystr += " VALUES " + self.replaceQuestionsForValues(noidoninsert);
            print(mystr);
            return "" + mystr;
        elif (commandtypestr == "UPDATE"):
            mystr = "" + basecmdstr + " SET " + self.getNameEqualsColList() + " WHERE ";
            print(mystr);
            return "" + mystr;
        else: raise Exception("INVALID SQL COMMAND TYPE!");

#from models.__init__ import CURSOR, CONN;
#from models.mycol import MyCol;
#from models.mybase import MyBase;
class MyTable(MyBase):
    all = [];
    __tablename = "";
    __mycols = [MyCol("id", "INTEGER", True, False)];
    __mybase = MyBase(__tablename, __mycols);

    def __init__(self, id=None):
        #super().__init__(self.__tablename, self.__mycols);
        if (id == None): pass;
        else: self.setId(id);
    
    def setId(self, val):
        if (type(val) == int and (0 < val or val == 0)): self._id = val;
        else: raise Exception("id must be an integer!");

    def getId(self): return self._id;

    id = property(getId, setId);

    @classmethod
    def addCols(cls, mcolslist):
        #print(len(mcolslist));
        for col in mcolslist:
            cls.__mycols.append(col);
            #print(f"Added col: {col}");
        #print(cls.getBase().getColListAsString(True));
        return True;
    
    @classmethod
    def getBase(cls): return cls.__mybase;

    @classmethod
    def make_table(cls):
        cls.makeSureCallerTableIsSetUp();
        #CURSOR.execute("CREATE tablename (id INTEGER PRIMARY KEY, cola TYPEA FOREIGN KEY,
        #colb TYPEB, colc, TYPEC)");
        CURSOR.execute(cls.getBase().genSQLCommand("CREATE TABLE"));
        CONN.commit();

    @classmethod
    def makeSureCallerTableIsSetUp(cls):
        if (cls.getTableName() == ""): cls.inittable();

    @classmethod
    def delete_table(cls):
        cls.makeSureCallerTableIsSetUp();
        #CURSOR.execute("DROP TABLE tablename");
        CURSOR.execute(cls.getBase().genSQLCommand("DROP TABLE"));
        CONN.commit();
        cls.all.clear();

    @classmethod
    def getTableName(cls): return "" + cls.__tablename;

    @classmethod
    def setTableName(cls, val):
        cls.getBase().setTableName(val);
        cls.__tablename = cls.getBase().getTableName();
    
    @classmethod
    def create(cls, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        #print("cls constructor called inside of create()!");
        mitem = cls();
        #print("DONE with cls constructor now calling save()!");
        mitem.save(vals);
        cls.all.append(mitem);
        return mitem;
    
    @classmethod
    def getTableRowById(cls, mid):
        if (type(mid) == int and (mid == 0 or 0 < mid)):
            for item in cls.all:
                if (item.id == mid): return item;
            return None;
        else: raise Exception("mid must be a positive or zero integer!");

    def save(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        #res = CURSOR.execute("INSERT INTO tablename (cola, colb, colc) VALUES ?, ?, ?", (?, ?, ?)");
        print(vals);
        CURSOR.execute(MyTable.getBase().genSQLCommand("INSERT INTO"), vals);
        CONN.commit();
        self.setId(CURSOR.lastrowid);

    def update(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        mylist = [vals[i] for i in range(len(vals))];
        mylist.append(self.id);
        mynwvals = tuple(self.id);
        #CURSOR.execute("UPDATE tablename SET cola = ?, colb = ?, colc = ? WHERE id = ?", (?, ?, ?));
        CURSOR.execute(MyTable.getBase().genSQLCommand("UPDATE") + "id = ", mynwvals);
        CONN.commit();

    def delete(self):
        CURSOR.execute(MyTable.getBase().genSQLCommand("DELETE FROM") + "id = ?", (self.id,));
        CONN.commit();
        MyTable.all.remove(MyTable.getTableRowById(self.id));

    @classmethod
    def get_all(cls): return cls.all;

#from models.mycol import MyCol;
#from models.mytable import MyTable;
class Name(MyTable):
    __calledinittable = False;
    def __init__(self):
        super().__init__();
        Name.inittable();
        self.setMyText("");

    @classmethod
    def inittable(cls):
        if (Name.__calledinittable): return;
        cls.setTableName("something");
        print("calling addCols inside of Name class now!");
        cls.addCols([MyCol("mytext", "TEXT", False, False)]);
        print("done with addCols inside of Name class!");
        Name.__calledinittable = True;

    def setMyText(self, val):
        if (type(val) == str): self._mytext = "" + val;
        else: raise Exception("this must be a string!");

    def getMyText(self): return self._mytext;

    mytext = property(getMyText, setMyText);

    def __repr__(self):
        return f"<Name id={self.id} mytext={self.mytext}>";
    
#MyTable.__tablename;
#print(Name.getTableName());
#print(Name.all);
#print(Name.getBase().getColListAsString(True));
#Name.setTableName("something");
#if (False): Name.delete_table();
#Name.make_table();
#print("calling create on Name class!");
#mn = Name.create(("test",));
#print(mn.id);
#Name.delete_table();
#print(Name.all);
#mstr = input("Proceed: ");
#mn.delete();
#print(Name.all);
#Name.delete_table();
