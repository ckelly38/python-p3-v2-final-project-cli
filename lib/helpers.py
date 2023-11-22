# lib/helpers.py
from models.model_1 import Name;

def helper_1():
    print("Performing useful function#1.")

def isClsCorrectType(cls):
    return (cls == Name);# or cls == ?
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

def get_by_id(cls, mid):
    return cls.getTableRowById(mid);

def find_by_id(cls):
    mid = getIntInputFromUser("Enter the id: ");
    mitem = get_by_id(cls, mid);
    if (mitem == None): print(f"invalid id {mid} used here! No items found with that id!");
    else: print(mitem);
    return mitem;

def find_by(cls, typestr):
    mitem = None;
    if (type(typestr) == str): pass;
    else: raise Exception("typestring must be a string!");
    if (typestr == "ID"): mitem = find_by_id(cls);
    #elif (typestr == "NAME"): mitem = cls.find_by_name(input("Enter the name here: "));
    else: raise Exception("invalid typestring found and used here!");
    if (mitem == None): print("no items found!");
    else: print(mitem);
    return mitem;


def create(cls):
    if (isClsCorrectType(cls)):
        #get the inputs
        #then load them into the cls.create()
        pass;
    else: print("the class is not the correct type!");

def update(cls):
    if (isClsCorrectType(cls)):
        #first get the id input from the user
        #then get the item by id
        #then get the other inputs
        #then load them into the cls.update(params);
        pass;
    else: print("the class is not the correct type!");

def delete(cls):
    if (isClsCorrectType(cls)):
        #first get the id input from the user
        #then get the item by id
        mitem = find_by_id(cls);
        #then call delete on the item: cls.delete();
        if (mitem == None): print("item not found!");
        else: mitem.delete();
    else: print("the class is not the correct type!");

def exit_program():
    print("Goodbye!")
    exit()
