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
from mybase import MyBase;#models.
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

class SwimLeague(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimleagues", SwimmerBase.getAllRequiredColumns());
    
    def __init__(self, vals):
        print("INSIDE SWIMLEAGUE CONSTRUCTOR!");
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a tuple!");
        self.setName(vals[0]);
        self.setAge(vals[1]);

    @classmethod
    def getRequiredTableName(cls): return "swimleagues";

    @classmethod
    def getRequiredAdditionalColumns(cls): return [];

    @classmethod
    def getAllRequiredColumns(cls): return super().getAllRequiredColumns();

    @classmethod
    def getBase(cls): return SwimLeague.__mybase;
    
    @classmethod
    def inittable(cls):
        if (SwimLeague.__calledinittable): return;
        #super().inittable(cls.getRequiredTableName(), True);
        SwimLeague.__calledinittable = True;

    def __repr__(self):
        return super().__repr__("SwimLeague");

    @classmethod
    def get_all(cls):
        return [item for item in SwimmerBase.get_all() if isinstance(item, SwimLeague)];

    #get all the teams in the league
    #need to be able to get all of swimmers in the league

class SwimTeam(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimteams", SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), [MyCol("LeagueID", "INTEGER", False, False)]));#True

    def __init__(self, vals):
        print("INSIDE SWIMTEAM CONSTRUCTOR!");
        #super().__init__(vals);
        #SwimTeam.inittable();
        self.setName(vals[0]);
        self.setAge(vals[1]);
        self.setLeagueId(vals[2]);
    
    @classmethod
    def getBase(cls): return SwimTeam.__mybase;

    @classmethod
    def getRequiredTableName(cls): return "swimteams";

    @classmethod
    def getRequiredAdditionalColumns(cls): return [MyCol("LeagueID", "INTEGER", False, False)];#True

    @classmethod
    def getAllRequiredColumns(cls):
        return SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), SwimTeam.getRequiredAdditionalColumns());

    @classmethod
    def inittable(cls):
        if (SwimTeam.__calledinittable): return;
        #super().inittable(cls.getRequiredTableName(), True);
        #cls.addCols(SwimTeam.getRequiredAdditionalColumns());
        SwimTeam.__calledinittable = True;

    def setLeagueId(self, val):
        if (type(val) == int and (0 < val or val == 0)): self._leagueid = val;
        else: raise Exception("league id must be an integer!");

    def getLeagueId(self): return self._leagueid;

    leagueid = property(getLeagueId, setLeagueId);

    def __repr__(self):
        return super().__repr__("SwimTeam");

    @classmethod
    def get_all(cls):
        return [item for item in SwimmerBase.get_all() if isinstance(item, SwimTeam)];

    #need to be able to get all of the swimmers on the team
    #need to be able to get the league
    #need to be able to find team by age or name or id

class Swimmer(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimmers", SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), [MyCol("TeamID", "INTEGER", False, False)]));#True
    
    def __init__(self, vals):
        print("INSIDE SWIMMER CONSTRUCTOR!");
        #super().__init__(vals);
        #Swimmer.inittable();
        self.setName(vals[0]);
        self.setAge(vals[1]);
        self.setTeamId(vals[2]);
    
    @classmethod
    def getBase(cls): return Swimmer.__mybase;

    @classmethod
    def getRequiredTableName(cls): return "swimmers";

    @classmethod
    def getRequiredAdditionalColumns(cls): return [MyCol("TeamID", "INTEGER", False, False)];#True

    @classmethod
    def getAllRequiredColumns(cls):
        return SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), Swimmer.getRequiredAdditionalColumns());

    @classmethod
    def inittable(cls):
        if (Swimmer.__calledinittable): return;
        #super().inittable(cls.getRequiredTableName(), True);
        #cls.addCols(Swimmer.getRequiredAdditionalColumns());
        Swimmer.__calledinittable = True;

    def setTeamId(self, val):
        if (type(val) == int and (0 < val or val == 0)): self._teamid = val;
        else: raise Exception("team id must be an integer!");

    def getTeamId(self): return self._teamid;

    teamid = property(getTeamId, setTeamId);

    def __repr__(self):
        return super().__repr__("Swimmer");

    @classmethod
    def get_all(cls):
        return [item for item in SwimmerBase.get_all() if isinstance(item, Swimmer)];

    #need to be able to get the league
    #need to be able to get the team
    #need to be able to find swimmer by age or name or id

#MyTable.__tablename;

#how many and what instances do we want?
#GOAL: each instance of SwimLeague, SwimTeam, and Swimmer all represent rows on their respective tables.
#GOAL: WHEN WE CALL MAKE_TABLE() A NEW TABLE IS CREATED...
#MAKE_TABLE() IS A CLASS METHOD.
#If we call make_table(), we need some way of knowing if a table was already created with that name.
#Calling make_table() geneates the SQL command in MYBASE class, but how to get the needed table name?
#Each class has a special method called getRequiredTableName().

#we need a new instance of Base to hold the columns and the tablename.
#just like we have a required tablename, should we have a required columns method?
#or was that the make_table?

#IT SEEMS THE BASE CLASS IS NOT BEING RECREATED...
#when do we want a row created?
#obviously when we do: varname = ClassName(params);
#when do we want a new table created?
#REQUIREMENT: the table should have the name of the table.
#MYBASE class can generate SQL commands based on a given type.
#But the MYBASE class needs the table name.
#CREATE() calls the calling CLASS'S CONSTRUCTOR.
#MAKE_TABLE() SUPPOSEDLY CREATES THE NEW TABLE.

print(SwimmerBase.getTableName());
print(SwimmerBase.all);
print(SwimmerBase.getBase().getColListAsString(True));
print();
print("NOW ATTEMPT TO CREATE A NEW SWIMMERBASE TABLE!");
if (True): SwimmerBase.delete_table();
SwimmerBase.make_table();
print("SUCCESSFULLY CREATED A NEW SWIMMERBASE TABLE!");
print();
print("calling create on SwimmerBase class!");
mn = SwimmerBase.create(("test", 0));
print(mn.id);
print(SwimmerBase.all);
print(SwimmerBase.getTableRowById(1));
print();
print("TESTING THE UPDATE METHOD NOW!");
mn.setName("other");
mn.update(("other", 0));
omn = SwimmerBase.create(("myself", 0));
print(omn.id);
print(SwimmerBase.all);
print(SwimmerBase.getTableRowById(1));
print(SwimmerBase.getTableRowById(2));
print("UPDATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMLEAGUES TABLE NOW!");
if (True): SwimLeague.delete_table();
SwimLeague.make_table();
mhsl = SwimLeague.create(("Mountain High Swim League", 40));
#print(SwimLeague.all);#returns SwimmerBase.all
print(SwimLeague.get_all());#returns only the SwimLeague instances
print("SWIMLEAGUE TABLE CREATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMTEAMS TABLE NOW!");
if (True): SwimTeam.delete_table();
SwimTeam.make_table();
dwd = SwimTeam.create(("Dam West Dolphins", 40, mhsl.id));
#print(SwimTeam.all);#returns SwimmerBase.all
print(SwimTeam.get_all());#returns only the SwimTeam instances
print("SWIMTEAM TABLE CREATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMMERS TABLE NOW!");
if (True): Swimmer.delete_table();
Swimmer.make_table();
bro = Swimmer.create(("Eric Kelly", 18, dwd.id));
#print(Swimmer.all);#returns SwimmerBase.all
print(Swimmer.get_all());#returns only the Swimmer instances
print("SWIMMERS TABLE CREATED SUCCESSFULLY!");
print();
print("BEGIN CLEAN UP NOW!");
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
print(SwimmerBase.all);
print(mn);
mn.delete();
print(SwimmerBase.all);
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
omn.delete();
mhsl.delete();
SwimmerBase.delete_table();
print("DONE CLEANING UP!");
