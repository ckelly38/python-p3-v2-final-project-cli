from swimmer import Swimmer;
from swimmerbase import SwimmerBase;
from swimteam import SwimTeam;
from swimleague import SwimLeague;


#MyTable.__tablename;

#how many and what instances do we want?
#GOAL: each instance of SwimLeague, SwimTeam, and Swimmer all represent rows on their respective tables.
#GOAL: WHEN WE CALL MAKE_TABLE() A NEW TABLE IS CREATED...
#MAKE_TABLE() IS A CLASS METHOD.
#If we call make_table(), we need some way of knowing if a table was already created with that name.
#Calling make_table() geneates the SQL command in MYBASE class, but how to get the needed table name?
#Each class has a special method called getRequiredTableName().

#we need a new instance of Base to hold the columns and the tablename.
#just like we have a required tablename, should we have a required columns method?
#or was that the make_table?

#IT SEEMS THE BASE CLASS IS NOT BEING RECREATED...
#when do we want a row created?
#obviously when we do: varname = ClassName(params);
#when do we want a new table created?
#REQUIREMENT: the table should have the name of the table.
#MYBASE class can generate SQL commands based on a given type.
#But the MYBASE class needs the table name.
#CREATE() calls the calling CLASS'S CONSTRUCTOR.
#MAKE_TABLE() SUPPOSEDLY CREATES THE NEW TABLE.

print(SwimmerBase.getTableName());
print(SwimmerBase.all);
print(SwimmerBase.getBase().getColListAsString(True));
print();
print("NOW ATTEMPT TO CREATE A NEW SWIMMERBASE TABLE!");
if (True): SwimmerBase.delete_table();
SwimmerBase.make_table();
print("SUCCESSFULLY CREATED A NEW SWIMMERBASE TABLE!");
print();
print("calling create on SwimmerBase class!");
mn = SwimmerBase.create(("test", 0));
print(mn.id);
print(f"SwimmerBase.all = {SwimmerBase.all}");
print(SwimmerBase.getTableRowById(1));
print();
print("TESTING THE UPDATE METHOD NOW!");
mn.setName("other");
mn.update(("other", 0));
omn = SwimmerBase.create(("myself", 0));
print(omn.id);
print(f"NEW SwimmerBase.all = {SwimmerBase.all}");
print(SwimmerBase.getTableRowById(1));
print(SwimmerBase.getTableRowById(2));
print("UPDATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMLEAGUES TABLE NOW!");
if (True): SwimLeague.delete_table();
SwimLeague.make_table();
mhsl = SwimLeague.create(("Mountain High Swim League", 40));
print(f"SwimLeague.all = {SwimLeague.all}");#returns SwimmerBase.all
print(f"SwimLeague.get_all() = {SwimLeague.get_all()}");#returns only the SwimLeague instances
print("SWIMLEAGUE TABLE CREATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMTEAMS TABLE NOW!");
if (True): SwimTeam.delete_table();
SwimTeam.make_table();
dwd = SwimTeam.create(("Dam West Dolphins", 40, mhsl.id));
print(f"SwimTeam.all = {SwimTeam.all}");#returns SwimmerBase.all
print(f"SwimTeam.get_all() = {SwimTeam.get_all()}");#returns only the SwimTeam instances
print("SWIMTEAM TABLE CREATED SUCCESSFULLY!");
print();
print("ATTEMPTING TO MAKE A SWIMMERS TABLE NOW!");
if (True): Swimmer.delete_table();
Swimmer.make_table();
bro = Swimmer.create(("Eric Kelly", 18, dwd.id));
ohr = Swimmer.create(("Micala", 18, dwd.id));
print(f"Swimmer.all = {Swimmer.all}");#returns SwimmerBase.all
print(f"Swimmer.get_all() = {Swimmer.get_all()}");#returns only the Swimmer instances
print("SWIMMERS TABLE CREATED SUCCESSFULLY!");
print();
print("TESTING OTHER METHODS NOW:");
print("GET THE TEAM THE SWIMMER IS ON:");
print(bro.team());
print("GET THE LEAGUE THE SWIMMER IS ON:");
print(bro.league());
print("GET THE SWIMMERS ON THE TEAM:");
print(bro.team().swimmers());
print("GET THE LEAGUE THE TEAM IS ON:");
print(bro.team().league());
print("GET THE TEAMS IN THE LEAGUE:");
print(bro.league().teams());
print("GET THE SWIMMERS IN THE LEAGUE:");
print(bro.league().swimmers());
print();
print("BEGIN CLEAN UP NOW!");
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
print(SwimmerBase.all);
print(mn);
mn.delete();
print(SwimmerBase.all);
mstr = input("Proceed: ");
if (mstr in ["1", "y", "Y", "yes", "Yes", "YES"]): pass;
else: exit();
omn.delete();
mhsl.delete();
SwimmerBase.delete_table();
print("DONE CLEANING UP!");
