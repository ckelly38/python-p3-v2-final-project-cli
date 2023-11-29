# lib/cli.py

from helpers import *;
from models.__init__ import CURSOR, CONN;
from models.swimmer import Swimmer;
from models.swimteam import SwimTeam;
from models.swimleague import SwimLeague;

#For EACH class in the data model, the CLI must include options:
#to create an object, delete an object, display all objects, view related objects, and
#find an object by attribute.

def genPartialMenuStrs(opts, bfrstr="", aftrstr=""):
    return [bfrstr + opts[i] + aftrstr for i in range(len(opts))];

def genMenuStrs():
    findoptsstrs = genPartialMenuStrs(["ID", "NAME", "AGE"], "Find an instance by ", " for ");
    crudoptsstrs = genPartialMenuStrs(["Create a new", "Update an", "Delete an"], "", " instance of ");
    #tablecrudsstrs = genPartialMenuStrs(["Create a", "Delete a"], "", " table for ");
    reloptsstrs = ["List the Swimmers on the SwimTeam", "List the SwimLeague for the SwimTeam",
         "List the Swimmers in the SwimLeague", "List the SwimTeams in the SwimLeague",
         "List the SwimTeam for the Swimmer", "List the SwimLeague for the Swimmer"];
    reloptsfuncs = [listSwimmersOnTeam, listSwimLeagueForTeam, listSwimmersForLeague,
                    listSwimTeamsForLeague, listSwimTeamForSwimmer, listSwimLeagueForSwimmer];
    findoptsfuncs = [find_by_id, find_by_name, find_by_age];
    crudfuncts = [create, update, delete];
    #tablecrudfuncts = [maketable, deltable];
    optsbeforefind = ["List all instances of "];
    functsoptsbeforefind = [list_all];
    myopts = [optsbeforefind, findoptsstrs, crudoptsstrs];#, tablecrudsstrs
    myfunctopts = [functsoptsbeforefind, findoptsfuncs, crudfuncts];#, tablecrudfuncts
    mytypes = ["Swimmer", "SwimTeam", "SwimLeague"];
    mstrs = [];
    mytypeclasses = [Swimmer, SwimTeam, SwimLeague];
    myfunccallsnotype = [];
    myfunccalltypeonly = [];
    for i in range(len(mytypes)):
        for n in range(len(myopts)):
            for k in range(len(myopts[n])):
                mstrs.append(myopts[n][k] + mytypes[i]);
                myfunccallsnotype.append(myfunctopts[n][k]);
                myfunccalltypeonly.append(mytypeclasses[i]);
    #, reloptsstrs, reloptsfuncs
    for i in range(len(reloptsstrs)):
        mstrs.append(reloptsstrs[i]);
        myfunccallsnotype.append(reloptsfuncs[i]);
        myfunccalltypeonly.append(None);
    return [mstrs, myfunccallsnotype, myfunccalltypeonly];

def main(menustrs):
    menu(menustrs);
    while True:
        choice = input("> ");
        if (choice in ["0", "quit", "exit", "q", "e", "QUIT", "EXIT", "Quit", "Exit"]): exit_program();
        elif (choice in ["1", "help", "h", "Help", "HELP", "?"]): menu(menustrs);
        else:
            mnum = -1;
            noerror = True;
            try:
                mnum = int(choice);
            except:
                noerror = False;
                print("Invalid choice! Your choice must be a number ");
                print("(unless you want the \"quit\" or \"help\" options)!");
            if (noerror):
                maxnumcs = len(menustrs[0]) + 2 - 1;
                if (mnum < 2 or maxnumcs < mnum):
                    print("Invalid choice! Number is out of range (0-" + str(maxnumcs) + " (inclusive))!");
                else:
                    funcinvoked = False;
                    for n in range(len(menustrs[1])):
                        if mnum == n + 2:
                            if (menustrs[2][n] == None): menustrs[1][n]();
                            else: menustrs[1][n](menustrs[2][n]);
                            funcinvoked = True;
                            break;
                    if (funcinvoked): pass;
                    else: raise Exception("The function must have been invoked, but it was not!");

def menu(menustrs):
    print("Please select an option:");
    print("0. Exits the program (alternatives are: quit, Quit, Exit, EXIT, QUIT, q, e)");
    print("1. Displays this menu again (alternatives are: help, h, HELP, Help, ?)");
    for i in range(len(menustrs[0])):
        print(f"{i+2}. {menustrs[0][i]}.");


if __name__ == "__main__":
    #possible known issue:
    #when the application is closed and reopened there are no instances of the classes (objects),
    #however, there may be information saved on the database.
    #
    #solution 1: remove all of the information in the database. (applied)
    #solution 2: read in all information from the database and generate the instances from it.
    #(not applied)
    #solution 3: serialize and deserialize objects when needed... (not applied)
    #
    #solution 2 may be better, but it is not applied; making us wonder
    #why we even have the database in the first place?
    #
    #startWithBlankDB();#sollution #1
    syncDB();
    main(genMenuStrs());
