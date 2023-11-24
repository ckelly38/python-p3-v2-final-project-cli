from __init__ import CURSOR, CONN;#models.
from mycol import MyCol;#models.
from mybase import MyBase;#models.
class MyTable(MyBase):
    all = [];
    __tablename = "";
    __mybase = None;
    __mycols = [MyCol("id", "INTEGER", True, False)];

    def __init__(self, id=None):
        #super().__init__(self.__tablename, self.__mycols);
        print("INSIDE MYTABLE CONSTRUCTOR!");
        if (id == None): pass;
        else: self.setId(id);

    def setId(self, val):
        if (type(val) == int and (0 < val or val == 0)): self._id = val;
        else: raise Exception("id must be an integer!");

    def getId(self): return self._id;

    id = property(getId, setId);

    @classmethod
    def getRequiredCols(cls): return [MyCol("id", "INTEGER", True, False)];

    @classmethod
    def addCols(cls, mcolslist):
        #print(len(mcolslist));
        for col in mcolslist:
            cls.__mycols.append(col);
            #print(f"Added col: {col}");
        #print(cls.getBase().getColListAsString(True));
        return True;
    
    @classmethod
    def makeBase(cls):
        MyTable.__mybase = MyBase(MyTable.__tablename, MyTable.__mycols);
        return MyTable.__mybase;

    @classmethod
    def getBase(cls):
        if (isinstance(MyTable.__mybase, MyBase)): return MyTable.__mybase;
        else: return MyTable.makeBase();

    @classmethod
    def make_table(cls):
        print(f"make_table calling class = cls = {cls}");
        cls.makeSureCallerTableIsSetUp();
        #CURSOR.execute("CREATE tablename (id INTEGER PRIMARY KEY, cola TYPEA FOREIGN KEY,
        #colb TYPEB, colc, TYPEC)");
        CURSOR.execute(cls.getBase().genSQLCommand("CREATE TABLE"));
        CONN.commit();

    @classmethod
    def makeSureCallerTableIsSetUp(cls):
        print(f"called inittable from MYTABLE class caller class = cls = {cls}");
        print(f"cls.getTableName() = {cls.getTableName()}");
        print(f"cls.getRequiredTableName() = {cls.getRequiredTableName()}");
        ctnm = cls.getTableName();
        rtnm = cls.getRequiredTableName();
        if (ctnm == "" or ctnm != rtnm): cls.inittable();

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
        print("INSIDE OF MYTABLE CREATE()!");
        print(f"cls = {cls}");
        print("cls constructor called inside of create()!");
        mitem = cls(vals);
        print("DONE with cls constructor now calling save()!");
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

    @classmethod
    def getById(cls, mid): return cls.getTableRowById(mid);

    def save(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        #res = CURSOR.execute("INSERT INTO tablename (cola, colb, colc) VALUES ?, ?, ?", (?, ?, ?)");
        print(vals);
        CURSOR.execute(self.getBase().genSQLCommand("INSERT INTO"), vals);
        CONN.commit();
        self.setId(CURSOR.lastrowid);

    def update(self, vals):
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a defined tuple!");
        mylist = [vals[i] for i in range(len(vals))];
        mylist.append(self.id);
        mynwvals = tuple(mylist);
        #CURSOR.execute("UPDATE tablename SET cola = ?, colb = ?, colc = ? WHERE id = ?", (?, ?, ?));
        CURSOR.execute(MyTable.getBase().genSQLCommand("UPDATE") + "id = ?", mynwvals);
        CONN.commit();

    def delete(self):
        CURSOR.execute(MyTable.getBase().genSQLCommand("DELETE FROM") + "id = ?", (self.id,));
        CONN.commit();
        MyTable.all.remove(MyTable.getTableRowById(self.id));

    @classmethod
    def get_all(cls): return cls.all;
