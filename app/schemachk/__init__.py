'''
Main calls the Looper once to loop on all rchk and then another looper to loop on all schk
Looper loops on all the files.
For each file it will create a TableList.
For each line in the file it will call the RuleParser
RuleParser will return an object including the SQL that needs to run to validate the rule
TableList will take in the rule object and attach it to a specific tables, or all tables
   
At end of file processing, Main will call a looper on the TableList and run the rules, generate a report (Render Object-> stdio,email,file)
'''
from app.schemachk.looper import ParseLooper
def run(parser):
    SchemCheker = ParseLooper(parser,file_postfix=".rchk")
    SchemCheker.run()
    for TableList in SchemCheker.getTableLists():
        #print("Start running rules for .rchk files")
        #print(TableList.tables_list)
        pass
     
    SchemCheker = ParseLooper(parser,file_postfix=".schk")
    SchemCheker.run()
    for TableList in SchemCheker.getTableLists():
        #print("Start running rules for .schk files")
        #print(TableList.tables_list)
        pass
        