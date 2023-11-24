#create
#list all
#update objects
#delete
#constructor
#find by id
#view related objects

#A Swim League has Many Swim Teams
#A Swim Team has Many Swimmers
#
#A Swim Leage has a name, an ID, an age, and people to manage it
#
#A Swim Team has a name, an ID, an age, equipment, people to manage it and meets
#
#A Swimmer has a name, an ID, an age, equipment, and parents to manage it.

#from __init__ import CURSOR, CONN;#models.
from mycol import MyCol;#models.
from mytable import MyTable;#models.
class SwimmerBase(MyTable):
    __calledinittable = False;
    def __init__(self, vals):
        print("INSIDE SWIMMERBASE CONSTRUCTOR!");
        super().__init__();
        SwimmerBase.inittable();
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a tuple!");
        self.setName(vals[0]);
        self.setAge(vals[1]);

    @classmethod
    def getRequiredTableName(cls): return "something";

    @classmethod
    def getRequiredAdditionalColumns(cls):
        return [MyCol("name", "TEXT", False, False), MyCol("age", "INTEGER", False, False)];

    @classmethod
    def combineTwoListsOfCols(cls, colsa, colsb):
        if (colsa == None or len(colsa) < 1): return colsb;
        elif (colsb == None or len(colsb) < 1): return colsa;
        myreclist = [];
        for rc in colsa: myreclist.append(rc);
        for rc in colsb: myreclist.append(rc);
        return myreclist;

    @classmethod
    def getAllRequiredColumns(cls):
        mcreccols = SwimmerBase.getRequiredAdditionalColumns();
        mtreccols = MyTable.getRequiredCols();
        return SwimmerBase.combineTwoListsOfCols(mtreccols, mcreccols);

    @classmethod
    def inittable(cls, tn = "something", useanyways = False):
        print(f"tn = {tn}");
        print(f"SwimmerBase.__calledinittable = {SwimmerBase.__calledinittable}");
        print(f"cls = {cls}");
        print(f"useanyways = {useanyways}");
        super().valMustBeBool(useanyways, "useanyways");
        if (SwimmerBase.__calledinittable and not useanyways): return;
        cls.setTableName(tn);
        print("calling addCols inside of SwimmerBase class now!");
        cls.addCols(SwimmerBase.getRequiredAdditionalColumns());
        print("done with addCols inside of SwimmerBase class!");
        SwimmerBase.__calledinittable = True;

    def setName(self, val):
        if (type(val) == str): self._name = "" + val;
        else: raise Exception("this must be a string!");

    def getName(self): return self._name;

    name = property(getName, setName);

    def setAge(self, val):
        if (type(val) == int):
            if (0 < val or val == 0): self._age = val;
            else: raise Exception("age must be a positive or zero integer!");
        else: raise Exception("age must be an integer!");

    def getAge(self): return self._age;

    age = property(getAge, setAge);

    def __repr__(self, clsname = "SwimmerBase"):
        return f"<{clsname} id={self.id} name={self.name} age={self.age}>";

    @classmethod
    def getAllMatchName(cls, nm):
        if (type(nm) == str and len(nm) > 0):
            return [item for item in cls.get_all() if item.getName() == nm];
        else: raise Exception("name must be a string and must not be empty!");

    @classmethod
    def getAllMatchAge(cls, age):
        if (type(age) == int and (0 < age or age == 0)):
            return [item for item in cls.get_all() if item.getAge() == age];
        else: raise Exception("age must be an integer and must not be negative!");
