#create
#list all
#update objects
#delete
#constructor
#find by id
#view related objects
from __init__ import CURSOR, CONN;
class MyCol:
    def __init__(self, colname, coltype, ispkey, isfkey):
        self.setColName(colname);
        self.setColType(coltype);
        self.setIsPKey(ispkey);
        self.setIsFKey(isfkey);
        self.errorCheckKeyValues();

    def getIsPOrFKey(self, usepkey):
        if (usepkey == True or usepkey == False):
            if (usepkey): return self._ispkey;
            else: return self._isfkey;
        else: raise Exception("invalid data type found and used for the type of keytouse!");

    def getIsPKey(self): return self.getIsPOrFKey(True);

    def getIsFKey(self): return self.getIsPOrFKey(False);

    def errorCheckKeyValues(self):
        if (self.getIsPKey() and self.getIsFKey()):
            raise Exception("key cannot be both a foreign and a primary key!");
        else: return True;

    def setIsPOrFKey(self, usepkey, val):
        if (usepkey == True or usepkey == False):
            if (val == True or val == False):
                if (usepkey): self._ispkey = val;
                else: self._isfkey = val;
            else: raise Exception("invalid data type found and used for the type of val!");
        else: raise Exception("invalid data type found and used for the type of keytouse!");

    def setIsPKey(self, val): self.setIsPOrFKey(True, val);

    def setIsFKey(self, val): self.setIsPOrFKey(False, val);

    ispkey = property(getIsPKey, setIsPKey);

    isfkey = property(getIsFKey, setIsFKey);

    def getStringProp(self, typestr):
        if (type(typestr) == str): pass;
        else: raise Exception("typestring must be a string!");
        if (typestr == "Name"): return self._colname;
        elif (typestr == "Type"): return self._coltype;
        else: raise Exception("invalid varible name used here!");

    def setStringProp(self, typestr, val):
        if (type(typestr) == str): pass;
        else: raise Exception("typestring must be a string!");
        if (type(val) == str and 0 < len(val)): pass;
        else: raise Exception("the value string must not be empty!");
        if (typestr == "Name"): self._colname = val;
        elif (typestr == "Type"): self._coltype = val;
        else: raise Exception("invalid varible name used here!");

    def setColName(self, val): self.setStringProp("Name", val);

    def getColName(self): return self.getStringProp("Name");

    colname = property(getColName, setColName);

    def setColType(self, val): self.setStringProp("Type", val);

    def getColType(self): return self.getStringProp("Type");

    coltype = property(getColType, setColType);

    def getIsKeyString(self):
        self.errorCheckKeyValues();
        if (self.ispkey): return "PRIMARY KEY";
        elif (self.isfkey): return "FOREIGN KEY";
        else: return "";
        
    def __repr__(self):
        kystr = self.getIsKeyString();
        if (len(kystr) < 1): return "" + self.colname + " " + self.coltype;
        else: return "" + self.colname + " " + self.coltype + " " + kystr;

    
    

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

    def valMustBeBool(self, val, varname = "var"):
        if (type(varname) == str and 0 < len(varname)): pass;
        else: raise Exception("varname must be a string with at least one character!");
        if (val == True or val == False): return True;
        else: raise Exception("" + varname + " must be a boolean value, but it was not");

    def getColListAsString(self, usefull, noid = False):
        self.valMustBeBool(usefull, "usefull");
        self.valMustBeBool(noid, "noid");
        mystr = "(";
        for n in range(len(self.cols)):
            skipcol = False;
            if (usefull):
                mystr += self.cols[n].__repr__();
                if (n + 1 < len(self.cols)): mystr += ", ";
            else:
                clnmstr = "" + self.cols[n].getColName();
                if (noid):
                    if (clnmstr == "id"): skipcol = True;
                    else: skipcol = False;
                if (skipcol): pass;
                else:
                    mystr += "" + clnmstr;
                    if (n + 1 < len(self.cols)): mystr += ", ";
        return mystr + ")";

    def getNameEqualsColList(self):
        mystr = "";
        for n in range(len(self.cols)):
            clnmstr = "" + self.cols[n].getColName();
            if (clnmstr == "id"): skipcol = True;
            else: skipcol = False;
            if (skipcol): pass;
            else:
                mystr += clnmstr + " = ?";
                if (n + 1 < len(self.cols)): mystr += ", ";
        return mystr;

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

    def replaceQuestionsForValues(self, noid = True):
        self.valMustBeBool(noid, "noid");
        for n in range(len(self.cols)):
            clnmstr = "" + self.cols[n].getColName();
            skipcol = False;
            if (noid):
                if (clnmstr == "id"): skipcol = True;
                else: skipcol = False;
            if (skipcol): pass;
            else:
                mystr += "?";
                if (n + 1 < len(self.cols)): mystr += ", ";
        return mystr;

    def genSQLCommand(self, commandtypestr, noidoninsert = True):
        self.valMustBeBool(noidoninsert, "noidoninsert");
        if (commandtypestr == "CREATE TABLE"):
            return "" + commandtypestr + " " + self.getTableName() + " " + self.getColListAsString(True);
        elif (commandtypestr == "DELETE FROM"):
            return "" + commandtypestr + " " + self.getTableName() + " WHERE "; 
        elif (commandtypestr == "DROP TABLE"):
            return "" + commandtypestr + " " + self.getTableName();
        elif (commandtypestr == "INSERT INTO"):
            mystr = "" + commandtypestr + " " + self.getTableName() + " ";
            if (noidoninsert): mystr += self.getColListAsString(False, True);
            else: mystr += self.getColListAsString(False, False);
            mystr +=  " VALUES " + self.replaceQuestionsForValues(noidoninsert);
            return "" + mystr;
        elif (commandtypestr == "UPDATE"):
            mystr = "" + commandtypestr + " " + self.getTableName() + " SET ";
            mystr += "" + self.getNameEqualsColList() + " WHERE ";
            return mystr;
        else: raise Exception("INVALID SQL COMMAND TYPE!");


class MyTable(MyBase):
    all = [];
    __tablename = "";
    __mycols = [MyCol("id", "INTEGER", True, False)];
    __mybase = MyBase(__tablename, __mycols);

    def __init__(self, id=None):
        if (id == None): pass;
        else: self.setId(id);
    
    def setId(self, val):
        if (type(val) == int and (0 < val or val == 0)): self.id = val;
        else: raise Exception("id must be an integer!");

    def getId(self): return self._id;

    id = property(getId, setId);

    @classmethod
    def addCols(cls, mcolslist):
        for col in mcolslist:
            cls.__mycols.append(col);
        return True;
    
    @classmethod
    def getBase(cls): return cls.__mybase;

    @classmethod
    def make_table(cls):
        #CURSOR.execute("CREATE tablename (id INTEGER PRIMARY KEY, cola TYPEA FOREIGN KEY,
        #colb TYPEB, colc, TYPEC)");
        CURSOR.execute(cls.getBase().genSQLCommand("CREATE TABLE"));
        CONN.commit();

    @classmethod
    def delete_table(cls):
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
        mitem = cls();
        mitem.save(vals);
        cls.all[mitem.id] = mitem;
    
    def save(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        #res = CURSOR.execute("INSERT INTO tablename (cola, colb, colc) VALUES ?, ?, ?", (?, ?, ?)");
        CURSOR.execute(super().genSQLCommand("INSERT INTO"), vals);
        CONN.commit();
        self.setId(CURSOR.lastrowid);

    def update(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        mylist = [vals[i] for i in range(len(vals))];
        mylist.append(self.id);
        mynwvals = tuple(self.id);
        #CURSOR.execute("UPDATE tablename SET cola = ?, colb = ?, colc = ? WHERE id = ?", (?, ?, ?));
        CURSOR.execute(super().genSQLCommand("UPDATE") + "id = ", mynwvals);
        CONN.commit();

    def delete(self):
        CURSOR.execute(super().genSQLCommand("DELETE FROM") + "id = ?", (self.id,));
        CONN.commit();
        MyTable.all.remove(all[self.id]);

class Name(MyTable):
    def __init__(self):
        super().__init__();
        Name.setTableName("something");
        super().addCols([MyCol("mytext", "TEXT", False, False)]);
    
#MyTable.__tablename;
#print(Name.getTableName());
#print(Name.all);
#mn = Name();
#print(Name.getBase().getColListAsString(True));
#mn.make_table();
#mn.delete_table();
