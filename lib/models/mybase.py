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


    def genSelectSQLCommand(self, colnames=[], tablenames=[], unique=False, useallcols=False,
                            addwhere=False):
        #SELECT * FROM tablenames WHERE ...
        #SELECT cola, colb, colc, FROM tablename WHERE ...
        #SELECT tablenamea.cola, tablenameb.colb, tablenameb.colc, FROM tablenames WHERE ...
        basecmdstr = "SELECT ";
        if (unique): basecmdstr += "DISTINCT ";
        tnmslen = len(tablenames);
        cnmslen = len(colnames);
        usedot = False;
        if (useallcols):
            if (cnmslen < 1): pass;
            else: raise Exception("when using all columns the colnames must not be provided!");
        else:
            if (cnmslen < 1): raise Exception("there must be at least one colname!");
        if (tnmslen > 1):
            if (tnmslen == cnmslen): usedot = True;
            else:
                if (useallcols): pass;
                else:
                    raise Exception("column names must be equal to table names length for more than one!");
        elif (tnmslen == 1): pass;
        else: raise Exception("there must be at least one tablename!");
        atleasttwotablenames = False;
        if (tnmslen > 1):
            for i in range(tnmslen):
                for k in range(i + 1, tnmslen):
                    if (tablenames[i] == tablenames[k]): pass;
                    else:
                        atleasttwotablenames = True;
                        break;
                if (atleasttwotablenames): break;
            if (atleasttwotablenames): pass;
            else:
                raise Exception("there must be at least 2 unique tablenames if there are at least 2 " +
                                "tablenames given! Duplicate names are not allowed, unless at least 2 " +
                                "unique tablenames are present!");
        colsstr = "";
        for i in range(cnmslen):
            if (usedot): colsstr += colnames[i] + "." + tablenames[i];
            else: colsstr += colnames[i];
            if (i + 1 < cnmslen): colsstr += ", ";
        tnmsstr = "";
        for i in range(tnmslen):
            tnmsstr += tablenames[i];
            if (i + 1 < tnmslen): tnmsstr += ", ";
        mystr = "" + basecmdstr + colsstr + " FROM " + tnmsstr;
        if (addwhere): mystr += " WHERE ";
        return mystr;

    def genSQLCommand(self, commandtypestr, noidoninsert = True):
        self.valMustBeBool(noidoninsert, "noidoninsert");
        tnm = self.getTableName();
        basecmdstr = "" + commandtypestr + " " + tnm;
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
        elif (commandtypestr == "PRAGMA"):
            mystr = "" + commandtypestr + " table_info(" + tnm + ")";
        else: raise Exception("INVALID SQL COMMAND TYPE!");
        #print(f"final command = {mystr}");
        return "" + mystr;