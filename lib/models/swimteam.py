from models.swimmerbase import SwimmerBase;#models.
from models.mybase import MyBase;#models.
from models.mycol import MyCol;#models.
from models.swimleague import SwimLeague;#models.
class SwimTeam(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimteams", SwimmerBase.combineTwoListsOfCols(
            SwimmerBase.getAllRequiredColumns(), [MyCol("LeagueID", "INTEGER", False, False)]));#True
    all = [];

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

    #@classmethod
    #def get_all(cls):
    #    return [item for item in SwimmerBase.get_all() if isinstance(item, SwimTeam)];

    def swimmers(self):
        from models.swimmer import Swimmer;
        return [swmr for swmr in Swimmer.get_all() if swmr.getTeamId() == self.getId()];

    def league(self): return SwimLeague.getById(self.leagueid);
