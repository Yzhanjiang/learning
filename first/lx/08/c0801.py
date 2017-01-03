#作业：通过ConfigParser模块修改samba的配置文件，添加如下内容：
#[public]
#comment = Public 
#path = /home/temp
#writable = yes


#coding_checker:UTF8

from ConfigParser import  ConfigParser
from string import  rstrip


class MysmbConf(ConfigParser):
    def __init__(self,config,**kw):
        ConfigParser.__init__(self, allow_no_value=True)
        self.config = config
        self.read(self.config)
        self.smbvars = {}
        print self.sections()
        self.set_mysmb_vars(kw)
        self.get_mysmb_vars()
           
    def set_mysmb_vars(self,kw):
        for k,v in kw.items():
#             print "k is %s,v is %s" %(k,v)
            setattr(self,k,v)
            self.smbvars[k] = v 
            
    def get_mysmb_vars(self):
        rst = {}
        if not self.has_section('public'):
            self.add_section('public')
        with open(self.config,'w') as fd:
            self.write(fd)
        options = self.options('public')
        for o in options:
            rst[o] = self.get('public',o)
        print "-" * 50
#         print  rst
#         print self.sections()
    def save(self):
        print self.smbvars  
        if not self.has_section('public'):
            self.add_section('public')
        for k,v in self.smbvars.items():
            self.set('public',k,v)
        with open(self.config,'w') as fd:
            self.write(fd)
        
if __name__ == "__main__":
    
    mc = MysmbConf('/root/smb.conf',aa='123',comment = 'Public' ,path = '/home/temp',writable = 'yes')
    print '*' * 50
    mc.save()
