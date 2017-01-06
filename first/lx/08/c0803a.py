#coding_checker:UTF8
from optparse import OptionParser
import  os
import sys 
from IPython.utils.io import stderr
import cmd
DIRNAME = os.path.dirname(__file__)
OPSTOOLS = os.path.abspath(os.path.join(DIRNAME,'..'))
sys.path.append(OPSTOOLS)
from subprocess import   Popen,PIPE
import  shlex
import  time
print OPSTOOLS
print "OPSTOOLS"
# print sys.path
from c0803b import MySQLDConfig

MYSQL_DATA_DIR = '/data/mysql1/mysqlmanage/data'
MYSQL_CONF_DIR = '/data/mysql1/mysqlmanage/conf'

def opt():
    parser = OptionParser()
    parser.add_option("-n","--name",
                      dest="name",
                      action="store",
                      default="myinstance"
                      )
    parser.add_option("-p","--port",
                      dest="port",
                      action="store",
                      default="3306"
                      )
    parser.add_option("-c","--command",
                      dest="command",
                      action="store",
                      default="check"
                      )
    options,args = parser.parse_args()
    return  options,args
    
def _init():
    if not os.path.exists(MYSQL_DATA_DIR):
        os.makedirs(MYSQL_DATA_DIR)
    if not os.path.exists(MYSQL_CONF_DIR):
        os.makedirs(MYSQL_CONF_DIR)

def readConfs():
    import  glob 
    confs = glob.glob(MYSQL_DATA_DIR+'/*.cnf')
    print confs
    print '22222'
    return confs

def checkPort(conf_file,port):
    mc = MySQLDConfig(conf_file)
    if mc.mysqld_vars['port'] == port:
        return True
    else:
        return False

def _genDict(name,port):
    return  {
            'pid-file': os.path.join(MYSQL_DATA_DIR,name,"%s.pid" %name),
            'sock':'/tmp/%s.sock' % name ,
            'port' : port,
            'datadir':os.path.join(MYSQL_DATA_DIR,name),
            'log-error':os.path.join(MYSQL_DATA_DIR,name,'%s.log' %name) 
             }   

def get_CNF(name):
    cnf = os.path.join(MYSQL_CONF_DIR,'%s.cnf' %name)
    return   cnf 

def mysql_install(name):
    cnf = get_CNF(name)
    cmd = 'mysql_install_db --defaults-file=%s' % cnf 
    print cmd
    p = Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)
    p.communicate()
    print p.returncode

def setOwner(datadir):
    os.system('chown mysql:mysql %s' % datadir)
    
def mysql_run(name):
    cnf = get_CNF(name)
    
    cmd = "mysqld_safe --defaults-file=%s &" %cnf
    print cmd 
    print shlex.split(cmd)
    p = Popen(cmd,stdout=PIPE,stderr=PIPE,shell=True)
    time.sleep(10)
    p.returncode

    
    
def createInstance(name,port):
    exists_confs = readConfs()
    print "11111"
    print exists_confs
    for conf in exists_confs:
        if conf.split('/')[-1][:-4] == name:
            print >> sys.stderr,"%s is exits" % name 
            sys.exit(-1)
        if checkPort(conf, port):
            print conf,port 
            print >> stderr,"%s is exits" %port 
            sys.exit(-1)
    cnf = os.path.join(MYSQL_CONF_DIR,'%s.cnf' % name)
    print cnf
    if not os.path.exists(cnf):
        c = _genDict(name, port)
        mc = MySQLDConfig(cnf,**c)
        mc.save()
    datadir = os.path.join(MYSQL_DATA_DIR,name)
    print datadir
    if not os.path.exists(datadir):
        mysql_install(name)
        setOwner(datadir)
        mysql_run(name)
            
if __name__ == '__main__':
    _init()
    options,args = opt()
    instance_name = options.name 
    instance_port = options.port 
    instance_cmd = options.command
    print instance_port,instance_name,instance_cmd
    if instance_cmd == 'create':
        createInstance(instance_name, instance_port)
    

#python   c0803a my02 -p 3309  -c create
    
    
