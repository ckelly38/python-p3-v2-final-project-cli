# lib/helpers.py
from models.swimmer import Swimmer;
from models.swimteam import SwimTeam;
from models.swimleague import SwimLeague;

def isClsCorrectType(cls):
    return (cls == Swimmer or cls == SwimTeam or cls == SwimLeague);# or cls == ?
    #return False;

def getTypeStringFrom(cls):
    if (cls == Swimmer): return "Swimmer";
    elif (cls == SwimTeam): return "SwimTeam";
    elif (cls == SwimLeague): return "SwimLeague";
    else: raise Exception("The class is not the correct type!");

def get_all(cls):
    if (isClsCorrectType(cls)): return cls.get_all();
    else: raise Exception("The class is not the correct type!");

def printItemHeaders(cls):
    if (cls == None): return;
    #ID|name|age|TeamID/LeagueID
    print("ID|Name|age", end="");
    if (cls == Swimmer): print("|TeamID");
    elif (cls == SwimTeam): print("|LeagueID");
    else: print();       

def printItem(item):
    if (item == None):
        print("None");
        return;
    else:
        print(str(item.id) + "|" + item.name + "|" + str(item.age), end="");
        if (type(item) == Swimmer): print("|" + str(item.teamid));
        elif (type(item) == SwimTeam): print("|" + str(item.leagueid));
        else: print();

def printItemWithHeaders(item):
    printItemHeaders(type(item));
    printItem(item);

def list_all(cls):
    mall = get_all(cls);
    if (mall == None or len(mall) < 1): print("No " + getTypeStringFrom(cls) + "s!");
    else:
        printItemHeaders(cls);
        for item in mall: printItem(item);
    
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

def findByNameIdOrAge(cls, typestr, pres = True):
    inptval = None;
    if (typestr == "id" or typestr == "age"): inptval = getIntInputFromUser("Enter the " + typestr +": ");
    elif (typestr == "name"): inptval = input("Enter the " + typestr + " here: ");
    else: raise Exception("Invalid typestring found and used here!");
    mitem = None;
    if (typestr == "id"): mitem = get_by_id(cls, inptval);
    elif (typestr == "age"): mitem = get_by_age(cls, inptval);
    else: mitem = get_by_name(cls, inptval);
    if ((mitem == None) or ((typestr in ["name", "age"]) and len(mitem) < 1)):
        print(f"Invalid {typestr} {inptval} used here! No {getTypeStringFrom(cls)}s found " +
              f"with that {typestr}!");
    else:
        if (pres): printItemWithHeaders(mitem);
    return mitem;

def find_by_id(cls, pres = True):
    return findByNameIdOrAge(cls, "id", pres);

def find_by_name(cls, pres = True):
    return findByNameIdOrAge(cls, "name", pres);

def find_by_age(cls, pres = True):
    return findByNameIdOrAge(cls, "age", pres);

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
        if (pres): printItemWithHeaders(mitem);
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
        if (mitem == None): print("Invalid id found and used for the swim team/swim league!");
        else:
            printItemHeaders(Swimmer);
            for s in mitem.swimmers(): printItem(s);
    else: print("The class is not the correct type!");

def listSwimmersOnTeam(): listSwimmersOn(SwimTeam);

def listSwimmersForLeague(): listSwimmersOn(SwimLeague);

def listSwimLeagueFor(cls):
    #first get the team
    #then get the swimmers
    mitem = find_by_id(cls, False);
    if (mitem == None): print("Invalid id found and used for the swim team!");
    else: printItemWithHeaders(mitem.league());

def listSwimLeagueForTeam(): listSwimLeagueFor(SwimTeam);

def listSwimLeagueForSwimmer(): listSwimLeagueFor(Swimmer);

def listSwimTeamsForLeague():
    lg = find_by_id(SwimLeague, False);
    if (lg == None): print("Invalid id found and used for the swim league!");
    else:
        tms = lg.teams();
        printItemHeaders(SwimTeam);
        for tm in tms: printItem(tm);

def listSwimTeamForSwimmer():
    s = find_by_id(Swimmer, False);
    if (s == None): print("Invalid id found and used for the swimmer!");
    else: printItemWithHeaders(s.team());

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
        printItemWithHeaders(mitem);
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
            printItemWithHeaders(mitem);
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
        if (cls.tableExists()):
            cls.delete_table();
            print("Table " + cls.getRequiredTableName() + " successfully removed!");
            return True;
        else:
            print("Table " + cls.getRequiredTableName() + " already removed!");
            return False;
    else: print("The class is not the correct type!");

def maketable(cls):
    if (isClsCorrectType(cls)):
        if (cls.tableExists()):
            print("Table " + cls.getRequiredTableName() + " already exists!");
            return False;
        else:
            cls.make_table();
            print("Table " + cls.getRequiredTableName() + " successfully created!");
        return True;
    else: raise Exception("The class is not the correct type!");

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

def tableexists(cls):
    if (isClsCorrectType(cls)):
        rval = cls.tableExists();
        if (rval): print("Yes! Table " + cls.getRequiredTableName() + " exists!");
        else: print("No! Table " + cls.getRequiredTableName() + " does not exist!");
        return rval;
    else: raise Exception("The class is not the correct type!");

def startWithBlankDB():
    #solution 1: remove all of the information in the database. (applied)
    dropalltables();
    makealltables();

def loadObjectsFromDB():
    #solution 2: read in all information from the database and generate the instances from it. (not applied)
    #need to know if the DB has the tables there or not
    #CURSOR.execute("PRAGMA table_info("tablename")").fetchall();
    #will return info if it exists; 0 rows if does not
    #maketable(cls) will throw an error if the table exists... if the table does not exist returns True.
    #wrote a tableExists() class method to do the pragma command to handle that problem
    #need to know how many items are on each table
    #need to know their IDs
    #need a way to get the information from the database
    #create() method could come in handy...
    #maybe the constructor will be used...
    #CURSOR.execute("SELECT * FROM tablename").fetchall() will be handy...

    #for each table:
    #if the table does not exist, make it.
    #if it does exist, read in data from it.
    print("BEGIN LOADING THE DATA INTO THE PROGRAM FROM THE DATABASE NOW!");
    clsses = [SwimLeague, SwimTeam, Swimmer];
    for c in clsses:
        if (c.tableExists()):
            #read the data...
            print("READING IN THE DATA FROM THE DATABASE NOW FOR " + getTypeStringFrom(c) + "!");
            res = c.getAllDataFromDB();
            #print(res);
            if (len(res) < 1):
                print("no data to be read in! Table " + c.getRequiredTableName() + " does exist!");
            else:
                for items in res:
                    #print(items);
                    mvals = [];
                    if (len(items) > 1):
                        mvals = [items[i] for i in range(len(items)) if i != 0];
                    mvals.append(items[0]);
                    mitem = c.create(tuple(mvals), True);
                    printItemWithHeaders(mitem);
                    print("item created successfully!");
            print("DONE READING IN THE DATA FOR " + getTypeStringFrom(c) + "!");
        else:
            print("no data to be read in! Table " + c.getRequiredTableName() + " does not exist!");
            print("Now creating the table!");
            c.make_table();
            print("Successfully created the table!");
    print("DONE LOADING THE DATA INTO THE PROGRAM FROM THE DATABASE ON STARTUP!");

def syncDB():
    #startWithBlankDB();#solution #1
    loadObjectsFromDB();#solution #2
    pass;

def exit_program():
    print("Goodbye!");
    exit();
