#coding:UTF8
from ConfigParser import  ConfigParser
import os 

class MySQLDConfig(ConfigParser):
    def __init__(self,config,**kw):
        ConfigParser.__init__(self,allow_no_value=True)
        self.config = config 
        self.mysqld_vars = {}
        if os.path.exists(self.config):
            self.read(self.config)
            self.get_mysqld_vars()
        else:
            self.get_defaults_mysqld_vars()
        self.set_mysql_vars(kw)
    
    def set_mysql_vars(self,kw):
        for k,v in kw.items():
            setattr(self,k,v)
            self.mysqld_vars[k] = v
     
           
    def get_mysqld_vars(self):
        rst = {}
        options = self.options('mysqld')
        for o in options:
            rst[o] = self.get('mysqld',o)
        self.set_mysql_vars(rst)
        
    def get_defaults_mysqld_vars(self):
        defaults = {
                'user':'mysql',
                'port':'3306',
                'skip-external-locking':None,
                'key_buffer':'16M',
                'max_allowed_packet':'16M',
                'thread_stack':'192K',
                'thread_cache_size':'8',
                'myisam-recover':'BACKUP',
                'max_connections':'100',
                'thread_concurrency':'10',
                'query_cache_limit':'1M',
                'query_cache_size':'16M',
                'log_error':'error.log',
                    }
        
        
        
        self.set_mysql_vars(defaults)
        
    def set_vars(self,k,v):
        self.mysqld_vars[k] = v 
        
    def save(self):
        if not self.has_section('mysqld'):
            self.add_section('mysqld')
        for k , v in self.mysqld_vars.iteritems():
            self.set('mysqld',k,v)
        print self.config
        with open(self.config,'w') as fd :
            self.write(fd)
        
if __name__ == '__main__':
    mc = MySQLDConfig(r'D:\my1.cnf',max_connections=200)
    mc.set_vars('skip-slave-start', None)
    mc.set_vars('port',3308)
    mc.save()

