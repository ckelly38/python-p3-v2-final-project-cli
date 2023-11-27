# lib/helpers.py
from models.swimmer import Swimmer;
from models.swimteam import SwimTeam;
from models.swimleague import SwimLeague;

def isClsCorrectType(cls):
    return (cls == Swimmer or cls == SwimTeam or cls == SwimLeague);# or cls == ?
    #return False;

def get_all(cls):
    if (isClsCorrectType(cls)): return cls.get_all();
    else: raise Exception("The class is not the correct type!");

def list_all(cls):
    mall = get_all(cls);
    if (mall == None or len(mall) < 1): print("No items!");
    else:
        for item in mall: print(item);

def getIntInputFromUser(msg):
    if (type(msg) == str): pass;
    else: raise Exception("The input message must be of type string!");
    myint = -1;
    while True:
        try:
            myint = int(input(msg));
            break;
        except Exception as exc:
            print("This must be a number!");
    return myint;

def get_by_id(cls, mid): return cls.getTableRowById(mid);

def get_by_age(cls, age): return cls.getAllMatchAge(age);

def get_by_name(cls, name): return cls.getAllMatchName(name);

def find_by_id(cls, pres = True):
    mid = getIntInputFromUser("Enter the id: ");
    mitem = get_by_id(cls, mid);
    if (mitem == None): print(f"Invalid id {mid} used here! No items found with that id!");
    else:
        if (pres): print(mitem);
    return mitem;

def find_by_name(cls, pres = True):
    name = input("Enter the name here: ");
    mitem = get_by_name(cls, name);
    if (mitem == None): print(f"Invalid name {name} used here! No items found with that name!");
    else:
        if (pres): print(mitem);
    return mitem;

def find_by_age(cls, pres = True):
    age = getIntInputFromUser("Enter the age: ");
    mitem = get_by_age(cls, age);
    if (mitem == None): print(f"Invalid age {age} used here! No items found with that age!");
    else:
        if (pres): print(mitem);
    return mitem;


def find_by(cls, typestr, pres = True):
    mitem = None;
    if (type(typestr) == str): pass;
    else: raise Exception("Typestring must be a string!");
    if (typestr == "ID"): mitem = find_by_id(cls, pres);
    elif (typestr == "NAME"): mitem = find_by_name(cls, pres);
    elif (typestr == "AGE"): mitem = find_by_age(cls, pres);
    else: raise Exception("Invalid typestring found and used here!");
    if (mitem == None): print("No items found!");
    else:
        if (pres): print(mitem);
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
        mitem = find_by_id(cls, False);
        if (mitem == None): print("Invalid id found and used for the swim team/swimleague!");
        else:
            for s in mitem.swimmers(): print(s);
    else: print("The class is not the correct type!");

def listSwimmersOnTeam(): listSwimmersOn(SwimTeam);

def listSwimmersForLeague(): listSwimmersOn(SwimLeague);

def listSwimLeagueFor(cls):
    #first get the team
    #then get the swimmers
    mitem = find_by_id(cls, False);
    if (mitem == None): print("Invalid id found and used for the swim team!");
    else: print(mitem.league());

def listSwimLeagueForTeam(): listSwimLeagueFor(SwimTeam);

def listSwimLeagueForSwimmer(): listSwimLeagueFor(Swimmer);

def listSwimTeamsForLeague():
    lg = find_by_id(SwimLeague, False);
    if (lg == None): print("Invalid id found and used for the swim league!");
    else:
        tms = lg.teams();
        for tm in tms: print(tm);

def listSwimTeamForSwimmer():
    s = find_by_id(Swimmer, False);
    if (s == None): print("Invalid id found and used for the swimmer!");
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
        print("Successfully created the item!");
    else: print("The class is not the correct type!");

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
        if (mitem == None): print(f"No instance of the class found with that id ({usrinputs[0]})!");
        else:
            mitem.setName(usrinputs[1]);
            mitem.setAge(usrinputs[2]);
            if (cls == SwimLeague): mitem.update((usrinputs[1], usrinputs[2]));
            else:
                if (cls == Swimmer): mitem.setTeamId(usrinputs[3]);
                else: mitem.setLeagueId(usrinputs[3]);
                mitem.update((usrinputs[1], usrinputs[2], usrinputs[3]));
            print(mitem);
            print("Successfully updated the item!");
    else: print("The class is not the correct type!");

def delete(cls):
    if (isClsCorrectType(cls)):
        #first get the id input from the user
        #then get the item by id
        mitem = find_by_id(cls);
        #then call delete on the item: cls.delete();
        if (mitem == None): print("Item not found!");
        else: mitem.delete();
        print("Item successfully deleted!");
    else: print("The class is not the correct type!");

def deltable(cls):
    if (isClsCorrectType(cls)):
        cls.delete_table();
        #print("Table successfully removed!");
    else: print("The class is not the correct type!");

def maketable(cls):
    if (isClsCorrectType(cls)):
        cls.make_table();
        #print("Table successfully created!");
    else: print("The class is not the correct type!");

def dropalltables():
    try:
        deltable(Swimmer);
    except:
        #print("No swimmers!");
        pass;
    try:
        deltable(SwimTeam);
    except:
        #print("No swim teams!");
        pass;
    try:
        deltable(SwimLeague);
    except:
        #print("No swim leagues!");
        pass;

def makealltables():
    try:
        maketable(Swimmer);
    except:
        #print("The swimmers table already created!");
        pass;
    try:
        maketable(SwimTeam);
    except:
        #print("The swimteams table already created!");
        pass;
    try:
        maketable(SwimLeague);
    except:
        #print("The swimleagues table already created!");
        pass;

def exit_program():
    print("Goodbye!");
    exit();
