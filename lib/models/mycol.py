class MyCol:
    def __init__(self, colname, coltype, ispkey, isfkey):
        #print("INSIDE MYCOL CONSTRUCTOR!");
        self.setColName(colname);
        self.setColType(coltype);
        self.setIsPKey(ispkey);
        self.setIsFKey(isfkey);
        self.errorCheckKeyValues();

    def getIsPOrFKey(self, usepkey):
        if (usepkey == True or usepkey == False):
            if (usepkey): return self._ispkey;
            else: return self._isfkey;
        else: raise Exception("invalid data type found and used for the type of keytouse!");

    def getIsPKey(self): return self.getIsPOrFKey(True);

    def getIsFKey(self): return self.getIsPOrFKey(False);

    def errorCheckKeyValues(self):
        if (self.getIsPKey() and self.getIsFKey()):
            raise Exception("key cannot be both a foreign and a primary key!");
        else: return True;

    def setIsPOrFKey(self, usepkey, val):
        if (usepkey == True or usepkey == False):
            if (val == True or val == False):
                if (usepkey): self._ispkey = val;
                else: self._isfkey = val;
            else: raise Exception("invalid data type found and used for the type of val!");
        else: raise Exception("invalid data type found and used for the type of keytouse!");

    def setIsPKey(self, val): self.setIsPOrFKey(True, val);

    def setIsFKey(self, val): self.setIsPOrFKey(False, val);

    ispkey = property(getIsPKey, setIsPKey);

    isfkey = property(getIsFKey, setIsFKey);

    def getStringProp(self, typestr):
        if (type(typestr) == str): pass;
        else: raise Exception("typestring must be a string!");
        if (typestr == "Name"): return self._colname;
        elif (typestr == "Type"): return self._coltype;
        else: raise Exception("invalid varible name used here!");

    def setStringProp(self, typestr, val):
        if (type(typestr) == str): pass;
        else: raise Exception("typestring must be a string!");
        if (type(val) == str and 0 < len(val)): pass;
        else: raise Exception("the value string must not be empty!");
        if (typestr == "Name"): self._colname = val;
        elif (typestr == "Type"): self._coltype = val;
        else: raise Exception("invalid varible name used here!");

    def setColName(self, val): self.setStringProp("Name", val);

    def getColName(self): return self.getStringProp("Name");

    colname = property(getColName, setColName);

    def setColType(self, val): self.setStringProp("Type", val);

    def getColType(self): return self.getStringProp("Type");

    coltype = property(getColType, setColType);

    def getIsKeyString(self):
        self.errorCheckKeyValues();
        if (self.ispkey): return "PRIMARY KEY";
        elif (self.isfkey): return "FOREIGN KEY";
        else: return "";
        
    def __repr__(self):
        kystr = self.getIsKeyString();
        myretstr = "" + "" + self.colname + " " + self.coltype;
        if (len(kystr) < 1): return "" + myretstr;
        else: return "" + myretstr + " " + kystr;
