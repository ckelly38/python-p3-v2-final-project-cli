# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")

def isClsCorrectType(cls):
    #return (cls == ? or cls == ?);
    return False;

def get_all(cls):
    if (isClsCorrectType(cls)):
        pass;
    else: raise Exception("the class is not the correct type!");

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
        #then call delete on the item: cls.delete();
        pass;
    else: print("the class is not the correct type!");

def exit_program():
    print("Goodbye!")
    exit()
