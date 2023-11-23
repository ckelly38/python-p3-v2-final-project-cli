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
        super().__init__();
        SwimmerBase.inittable();
        if (type(vals) == tuple): pass;
        else: raise Exception("vals must be a tuple!");
        self.setName(vals[0]);
        self.setAge(vals[1]);

    @classmethod
    def getRequiredTableName(cls): return "something";

    @classmethod
    def inittable(cls, tn = "something", useanyways = False):
        print(f"tn = {tn}");
        print(f"SwimmerBase.__calledinittable = {SwimmerBase.__calledinittable}");
        print(f"cls = {cls}");
        super().valMustBeBool(useanyways, "useanyways");
        if (SwimmerBase.__calledinittable and not useanyways): return;
        cls.setTableName(tn);
        print("calling addCols inside of SwimmerBase class now!");
        cls.addCols([MyCol("name", "TEXT", False, False), MyCol("age", "INTEGER", False, False)]);
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
    
    @classmethod
    def getRequiredTableName(cls): return "swimleagues";
    
    @classmethod
    def inittable(cls):
        if (SwimLeague.__calledinittable): return;
        super().inittable(cls.getRequiredTableName(), True);
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
    def __init__(self, vals):
        super().__init__(vals);
        SwimTeam.inittable();
        self.setLeagueId(vals[2]);
    
    @classmethod
    def getRequiredTableName(cls): return "swimteams";

    @classmethod
    def inittable(cls):
        if (SwimTeam.__calledinittable): return;
        super().inittable(cls.getRequiredTableName(), True);
        cls.addCols([MyCol("LeagueID", "INTEGER", False, True)]);
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
    def __init__(self, vals):
        super().__init__(vals);
        Swimmer.inittable();
        self.setTeamId(vals[2]);
    
    @classmethod
    def getRequiredTableName(cls): return "swimmers";

    @classmethod
    def inittable(cls):
        if (Swimmer.__calledinittable): return;
        super().inittable(cls.getRequiredTableName(), True);
        cls.addCols([MyCol("TeamID", "INTEGER", False, True)]);
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
print(SwimmerBase.getTableName());
print(SwimmerBase.all);
print(SwimmerBase.getBase().getColListAsString(True));
if (True): SwimmerBase.delete_table();
SwimmerBase.make_table();
print("calling create on SwimmerBase class!");
mn = SwimmerBase.create(("test", 0));
print(mn.id);
print(SwimmerBase.all);
print(SwimmerBase.getTableRowById(1));
mn.setName("other");
mn.update(("other", 0));
omn = SwimmerBase.create(("myself", 0));
print(omn.id);
print(SwimmerBase.all);
print(SwimmerBase.getTableRowById(1));
print(SwimmerBase.getTableRowById(2));
SwimLeague.make_table();
mhsl = SwimLeague.create(("Mountain High Swim League", 40));
print(SwimLeague.all);#returns SwimmerBase.all
print(SwimLeague.get_all());#returns only the SwimLeague instances
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
mn.delete();
print(SwimmerBase.all);
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
omn.delete();
mhsl.delete();
SwimmerBase.delete_table();
