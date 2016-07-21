'''
Created on Jul 21, 2016

@author: itaymoav
'''



def parse_to_sql_factory(single_rule,db_name,verbosity):
    '''
    Factory function to instantiate, parse and return the correct SQL object
    '''

    # extract the rule name and params
    class_and_params = single_rule.split('[')
    try:
        params = class_and_params[1].replace(']','').split(',')
        
    except IndexError:
        params = []
        
    #instantiate the correct class (SqlRule+RuleName)
    SqlClass = globals()[class_and_params[0].capitalize().replace('_','')]
    return SqlClass(single_rule,db_name,params,verbosity)



class SQLReady():
    '''
    This class will hold the actual SQL to run for each singular rule parsed.
    Parses the string token into a SQL command
    '''
    
    def __init__(self,single_rule,db_name,params,verbosity):
        '''
        @param single_rule: string this is a single rule token from the file, Each line can have several rules space separated, this is only one.  
        @param db_name: string the db name to attach to each sql rule. this is the DB that comes from the file name parsed
        '''
        self.verbosity = verbosity
        self._single_rule = single_rule
        self.params = params
        self.db_name = db_name
        self.sql = ''
        self._generate_sql()
        
    def __str__(self):
        return "{}.{} ({}) : {}".format(self.db_name,self._single_rule,self.params,self.sql)
    
    def _generate_sql(self):
        '''
        generates the specific sql that will be used to validate the rule
        Populates __self__.sql
        ''' 
        raise NotImplementedError("You must implement _generate_sql in app.schemachk.sql_objects.{}".format(self.__class__.__name__))
    
    def test_rule(self,table_name):
        '''
        adds the foreign table name
        runs the sql
        tests the result to see the rule has been complied to
        @return boolean
        
        THIS IS AN ABSTRACT METHOD
        '''
        raise NotImplementedError("You must implement test_rule(table_name) in app.schemachk.sql_objects.{}".format(self.__class__.__name__))
     
     
     
     
     
     
class Exists(SQLReady):
    def _generate_sql(self):
        '''
        exists will verify input table exists in this db (just name)
        '''
        self.sql = "DESCRIBE {current_db}.[[table_name]]".format(current_db=self.db_name)
        return self
                 
                 
                 
                 
                  
class Same(SQLReady):
    def _generate_sql(self):
        '''
        exists will verify input table exists in this db (just name)
        '''
        self.sql = "DESCRIBE {current_db}.[[table_name]]".format(current_db=self.db_name)
        return self
    
    
    
    
    
class Notexists(SQLReady):
    def _generate_sql(self):
        '''
        exists will verify input table exists in this db (just name)
        '''
        self.sql = "DESCRIBE {current_db}.[[table_name]]".format(current_db=self.db_name)
        return self
    
    
    
    
    
class Fieldexists(SQLReady):
    def _generate_sql(self):
        '''
        exists will verify input table exists in this db (just name)
        '''
        self.sql = "DESCRIBE {current_db}.[[table_name]]".format(current_db=self.db_name)
        return self
    