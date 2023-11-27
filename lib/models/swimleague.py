from models.mybase import MyBase;#models.
from models.swimmerbase import SwimmerBase;#models.
class SwimLeague(SwimmerBase):
    __calledinittable = False;
    __mybase = MyBase("swimleagues", SwimmerBase.getAllRequiredColumns());
    all = [];
    
    def __init__(self, vals):
        #print("INSIDE SWIMLEAGUE CONSTRUCTOR!");
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

    #@classmethod
    #def get_all(cls):
    #    return [item for item in SwimmerBase.get_all() if isinstance(item, SwimLeague)];

    def teams(self):
        from models.swimteam import SwimTeam;
        return [tm for tm in SwimTeam.get_all() if tm.getLeagueId() == self.id];

    def swimmers(self):
        swmrsonlg = [];
        for tm in self.teams():
            mswmrs = tm.swimmers();
            for swmr in mswmrs:
                swmrsonlg.append(swmr);
        return swmrsonlg;
