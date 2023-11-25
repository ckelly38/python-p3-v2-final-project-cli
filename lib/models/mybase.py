from models.mycol import MyCol;#models.
class MyBase:
    def __init__(self, tablename = "", cols = None):
        #an array of colobjs
        #column name, type, ispkey, isfkey
        #print("INSIDE MYBASE CONSTRUCTOR!");
        self.setTableName(tablename);
        self.setCols(cols);
    
    def getTableName(self):
        if (type(self._tablename) == str and 0 < len(self._tablename)):
            return self._tablename;
        else: raise Exception("tablename must not be an empty string!");

    def setTableName(self, val):
        if (type(val) == str): self._tablename = val;
        else: raise Exception("tablename must be a string!");

    tablename = property(getTableName, setTableName);

    def setCols(self, val):
        if (val == None or len(val) < 1):
            if (self._cols == None): pass;
            else: self._cols.clear();
            self._cols = val;
        else:
            for item in val:
                if (isinstance(item, MyCol)): pass;
                else: raise Exception("the item must be of type MyCol, but it was not!");
        self._cols = val;
    
    def getCols(self): return self._cols;

    cols = property(getCols, setCols);

    @classmethod
    def valMustBeBool(cls, val, varname = "var"):
        if (type(varname) == str and 0 < len(varname)): pass;
        else: raise Exception("varname must be a string with at least one character!");
        if (val == True or val == False): return True;
        else: raise Exception("" + varname + " must be a boolean value, but it was not");

    def getColListAsString(self, usefull, noid = False, useaddstronly = False, addstr = ""):
        self.valMustBeBool(usefull, "usefull");
        self.valMustBeBool(noid, "noid");
        self.valMustBeBool(useaddstronly, "useaddstronly");
        if (type(addstr) == str): pass;
        else: raise Exception("addstring must be a string!");
        mystr = "(";
        for n in range(len(self.cols)):
            skipcol = False;
            if (usefull): mystr += self.cols[n].__repr__();
            else:
                clnmstr = "" + self.cols[n].getColName();
                if (noid):
                    if (clnmstr == "id"): skipcol = True;
                    else: skipcol = False;
                if (skipcol): pass;
                else:
                    if (useaddstronly): mystr += "" + addstr;
                    else: mystr += "" + clnmstr + "" + addstr;
            if ((n + 1 < len(self.cols)) and (usefull or not skipcol)): mystr += ", ";
        return mystr + ")";

    def getNameEqualsColList(self):
        mystr = self.getColListAsString(False, True, False, " = ?");
        #usefull False, noid True, useaddstronly False, addstr " = ?"
        return mystr[1:-1];#remove the () surrounding it

    def replaceQuestionsForValues(self, noid = True):
        #usefull False, noid True, useaddstronly True, addstr " = ?"
        return "" + self.getColListAsString(False, noid, True, "?");

    def genSQLCommand(self, commandtypestr, noidoninsert = True):
        self.valMustBeBool(noidoninsert, "noidoninsert");
        basecmdstr = "" + commandtypestr + " " + self.getTableName();
        #print(f"basecmdstr = {basecmdstr}");
        mystr = "";
        if (commandtypestr == "CREATE TABLE"):
            mystr = "" + basecmdstr + " " + self.getColListAsString(True);
        elif (commandtypestr == "DELETE FROM"):
            #print(basecmdstr + " WHERE ");
            mystr = "" + basecmdstr + " WHERE "; 
        elif (commandtypestr == "DROP TABLE"):
            #print(basecmdstr);
            mystr = "" + basecmdstr;
        elif (commandtypestr == "INSERT INTO"):
            mystr = "" + basecmdstr + " ";
            if (noidoninsert): mystr += self.getColListAsString(False, True, False, "");
            else: mystr += self.getColListAsString(False, False, False, "");
            mystr += " VALUES " + self.replaceQuestionsForValues(noidoninsert);
        elif (commandtypestr == "UPDATE"):
            mystr = "" + basecmdstr + " SET " + self.getNameEqualsColList() + " WHERE ";
        else: raise Exception("INVALID SQL COMMAND TYPE!");
        #print(f"final command = {mystr}");
        return "" + mystr;