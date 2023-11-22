# lib/cli.py

from helpers import *;
from models.__init__ import CURSOR, CONN;
from models.model_1 import Name;

#For EACH class in the data model, the CLI must include options:
#to create an object, delete an object, display all objects, view related objects, and
#find an object by attribute.

def genPartialMenuStrs(opts, bfrstr="", aftrstr=""):
    mstrs = [];
    for i in range(len(opts)):
        mstrs.append(bfrstr + opts[i] + aftrstr);
    return mstrs;

def genMenuStrs():
    findoptsstrs = genPartialMenuStrs(["ID"], "Find an instance by ", " for ");
    crudoptsstrs = genPartialMenuStrs(["Create a new", "Update an", "Delete an"], "", " instance of ");
    findoptsfuncs = [find_by_id];
    crudfuncts = [create, update, delete];
    optsbeforefind = ["List all instances of "];
    functsoptsbeforefind = [list_all];
    myopts = [optsbeforefind, findoptsstrs, crudoptsstrs];
    myfunctopts = [functsoptsbeforefind, findoptsfuncs, crudfuncts];
    mytypes = ["Name"];#, "typeb", "typec"
    mstrs = [];
    mytypeclasses = [Name];#, None, None
    myfunccallsnotype = [];
    myfunccalltypeonly = [];
    for i in range(len(mytypes)):
        for n in range(len(myopts)):
            for k in range(len(myopts[n])):
                mstrs.append(myopts[n][k] + mytypes[i]);
                myfunccallsnotype.append(myfunctopts[n][k]);
                myfunccalltypeonly.append(mytypeclasses[i]);  
    return [mstrs, myfunccallsnotype, myfunccalltypeonly];


def main(menustrs):
    while True:
        menu(menustrs)
        choice = input("> ")
        if choice == "0" or choice == "quit" or choice == "exit" or choice == "q": exit_program();
        elif choice == "1" or choice == "help" or choice == "h": pass;
        else:
            mnum = -1;
            noerror = True;
            try:
                mnum = int(choice);
            except Exception as exc:
                noerror = False;
                print("Invalid choice");
            if (noerror):
                if (mnum < 2 or len(menustrs[0]) + 2 - 1 < mnum): print("Invalid choice");
                else:
                    funcinvoked = False;
                    for n in range(len(menustrs[1])):
                        if mnum == n + 2:
                            menustrs[1][n](menustrs[2][n]);
                            funcinvoked = True;
                            break;
                    if (funcinvoked): pass;
                    else: raise Exception("the function must have been invoked, but it was not!");



def menu(menustrs):
    print("Please select an option:");
    print("0. Exits the program");
    print("1. Displays this menu again");
    for i in range(len(menustrs[0])):
        print(f"{i+2}. {menustrs[0][i]}.");


if __name__ == "__main__":
    main(genMenuStrs());
