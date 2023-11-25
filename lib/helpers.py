# lib/helpers.py
from models.swimmer import Swimmer;
from models.swimteam import SwimTeam;
from models.swimleague import SwimLeague;

def helper_1():
    print("Performing useful function#1.")

def isClsCorrectType(cls):
    return (cls == Swimmer or cls == SwimTeam or cls == SwimLeague);# or cls == ?
    #return False;

def get_all(cls):
    if (isClsCorrectType(cls)): return cls.get_all();
    else: raise Exception("the class is not the correct type!");

def list_all(cls):
    mall = get_all(cls);
    if (mall == None or len(mall) < 1): print("no items!");
    else:
        for item in mall:
            print(item);

def getIntInputFromUser(msg):
    if (type(msg) == str): pass;
    else: raise Exception("the input message must be of type string!");
    myint = -1;
    while True:
        try:
            myint = int(input(msg));
            break;
        except Exception as exc:
            print("this must be a number!");
    return myint;

def get_by_id(cls, mid): return cls.getTableRowById(mid);

def get_by_age(cls, age): return cls.getAllMatchAge(age);

def get_by_name(cls, name): return cls.getAllMatchName(name);

def find_by_id(cls):
    mid = getIntInputFromUser("Enter the id: ");
    mitem = get_by_id(cls, mid);
    if (mitem == None): print(f"invalid id {mid} used here! No items found with that id!");
    else: print(mitem);
    return mitem;

def find_by_name(cls):
    name = input("Enter the name here: ");
    mitem = get_by_name(cls, name);
    if (mitem == None): print(f"invalid name {name} used here! No items found with that name!");
    else: print(mitem);
    return mitem;

def find_by_age(cls):
    age = getIntInputFromUser("Enter the age: ");
    mitem = get_by_age(cls, age);
    if (mitem == None): print(f"invalid age {age} used here! No items found with that age!");
    else: print(mitem);
    return mitem;


def find_by(cls, typestr):
    mitem = None;
    if (type(typestr) == str): pass;
    else: raise Exception("typestring must be a string!");
    if (typestr == "ID"): mitem = find_by_id(cls);
    elif (typestr == "NAME"): mitem = find_by_name(cls);
    elif (typestr == "AGE"): mitem = find_by_age(cls);
    else: raise Exception("invalid typestring found and used here!");
    if (mitem == None): print("no items found!");
    else: print(mitem);
    return mitem;

def getAllUserInputs(noid=False, reqlgid=True, useleagueid=True, omsg=""):
    mid = -1;
    if (noid): pass;
    else: mid = getIntInputFromUser("Enter the id: ");
    name = input("Enter the " + omsg + "name here: ");
    age = getIntInputFromUser("Enter the " + omsg + "age: ");
    omid = -1;
    if (reqlgid):
        msg = "";
        if (useleagueid): msg = "league";
        else: msg = "team";
        omid = getIntInputFromUser("Enter the " + omsg + msg + " id: ");
    return [mid, name, age, omid];

def listSwimmersOn(cls):
    if (isClsCorrectType(cls)):
        mitem = find_by_id(cls);
        if (mitem == None): print("invalid id found and used for the swim team/swimleague!");
        else:
            for s in mitem.swimmers(): print(s);
    else: print("the class is not the correct type!");

def listSwimmersOnTeam(): listSwimmersOn(SwimTeam);

def listSwimmersForLeague(): listSwimmersOn(SwimLeague);

def listSwimLeagueFor(cls):
    #first get the team
    #then get the swimmers
    mitem = find_by_id(cls);
    if (mitem == None): print("invalid id found and used for the swim team!");
    else: print(mitem.league());

def listSwimLeagueForTeam(): listSwimLeagueFor(SwimTeam);

def listSwimLeagueForSwimmer(): listSwimLeagueFor(Swimmer);

def listSwimTeamsForLeague():
    lg = find_by_id(SwimLeague);
    if (lg == None): print("invalid id found and used for the swim league!");
    else: print(lg.teams());

def listSwimTeamForSwimmer():
    s = find_by_id(Swimmer);
    if (s == None): print("invalid id found and used for the swimmer!");
    else: print(s.team());

def create(cls):
    if (isClsCorrectType(cls)):
        #get the inputs excluding the id, because that does not exist yet
        #then load them into the cls.create()
        reqlgid = True;
        if (cls == SwimLeague): reqlgid = False;
        useleagueid = True;
        if (cls == Swimmer): useleagueid = False;
        usrinputs = getAllUserInputs(True, reqlgid, useleagueid);
        mitem = None;
        if (cls == SwimLeague): mitem = cls.create((usrinputs[1], usrinputs[2]));
        else: mitem = cls.create((usrinputs[1], usrinputs[2], usrinputs[3]));
        print(mitem);
        print("successfully created the item!");
    else: print("the class is not the correct type!");

def update(cls):
    if (isClsCorrectType(cls)):
        #first get the id input from the user
        #then get the item by id
        #then get the other inputs
        #then load them into the cls.update(params);
        reqlgid = True;
        if (cls == SwimLeague): reqlgid = False;
        useleagueid = True;
        if (cls == Swimmer): useleagueid = False;
        usrinputs = getAllUserInputs(False, reqlgid, useleagueid, "new ");
        mitem = get_by_id(cls, usrinputs[0]);
        if (mitem == None): print(f"no instance of the class found with that id ({usrinputs[0]})!");
        else:
            mitem.setName(usrinputs[1]);
            mitem.setAge(usrinputs[2]);
            if (cls == SwimLeague): mitem.update((usrinputs[1], usrinputs[2]));
            else:
                if (cls == Swimmer): mitem.setTeamId(usrinputs[3]);
                else: mitem.setLeagueId(usrinputs[3]);
                mitem.update((usrinputs[1], usrinputs[2], usrinputs[3]));
            print(mitem);
            print("successfully updated the item!");
    else: print("the class is not the correct type!");

def delete(cls):
    if (isClsCorrectType(cls)):
        #first get the id input from the user
        #then get the item by id
        mitem = find_by_id(cls);
        #then call delete on the item: cls.delete();
        if (mitem == None): print("item not found!");
        else: mitem.delete();
        print("item successfully deleted!");
    else: print("the class is not the correct type!");

def deltable(cls):
    if (isClsCorrectType(cls)):
        cls.delete_table();
        #print("table successfully removed!");
    else: print("the class is not the correct type!");

def maketable(cls):
    if (isClsCorrectType(cls)):
        cls.make_table();
        #print("table successfully created!");
    else: print("the class is not the correct type!");

def dropalltables():
    try:
        deltable(Swimmer);
    except:
        #print("no swimmers!");
        pass;
    try:
        deltable(SwimTeam);
    except:
        #print("no swim teams!");
        pass;
    try:
        deltable(SwimLeague);
    except:
        #print("no swim leagues!");
        pass;

def makealltables():
    try:
        maketable(Swimmer);
    except:
        #print("swimmers table already created!");
        pass;
    try:
        maketable(SwimTeam);
    except:
        #print("swimteams table already created!");
        pass;
    try:
        maketable(SwimLeague);
    except:
        #print("swimleagues table already created!");
        pass;

def exit_program():
    print("Goodbye!")
    exit()
