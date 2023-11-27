from models.mycol import MyCol;#models.
from models.mybase import MyBase;#models.
from models.swimmerbase import SwimmerBase;#models.
from models.swimteam import SwimTeam;#models.
class Swimmer(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimmers", SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), [MyCol("TeamID", "INTEGER", False, False)]));#True
    all = [];
    
    def __init__(self, vals):
        #print("INSIDE SWIMMER CONSTRUCTOR!");
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
        mystr = super().__repr__("Swimmer");
        return "" + mystr[0:-1] + f" teamid={self.teamid}" + mystr[-1:];

    #@classmethod
    #def get_all(cls):
    #    return [item for item in SwimmerBase.get_all() if isinstance(item, Swimmer)];

    def team(self):
        #print(self);
        #print(f"all swim teams: {SwimTeam.get_all()}");
        for tm in SwimTeam.get_all():
            #print(tm);
            if (tm.id == self.getTeamId()): return tm;
        return None;

    def league(self):
        tm = self.team();
        if (tm == None): return None;
        elif (isinstance(tm, SwimTeam)): return tm.league();
        else: raise Exception("tm must be of type SwimTeam, but it was not!");
