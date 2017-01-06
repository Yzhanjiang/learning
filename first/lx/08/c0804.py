#作业：
1. 把/var/log/messages存到数据里
按照logtime，hostname，program，msg等字段存储
如果日志文件过大，只存储最后300行
提示：使用正在表达式的有名称组。
2. 完善视频里面的mysql工具箱



#coding_checker:UTF8
import re 
from subprocess import Popen,PIPE
import shlex
from IPython.utils.io import stdout, stderr
import MySQLdb
import sys

def get_DATA():
    cmd = 'tail -n 300 /root/messages'
    print shlex.split(cmd)
    p = Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)
    stdout,stderr =  p.communicate()
    print "6" * 30
    print stdout
    return  stdout

def get_result(data):
    reg = re.compile(r'(?P<logtime>(\w+)\s+\d+\s[\d:]+)\s(?P<hostname>[\w\.]+)\s(?P<program>\w+(\[\d+\])?):(?P<msg>.*)')
    m = reg.search(data)
#     s = 'Jan  6 10:44:15 zhan192 freshclam[11504]: Downloading daily-22841.cdiff [100%]'
#     m = reg.search(s)
    if m:
#         print  m.groups()
        print m.groupdict() 
        return  m.groupdict() 
    else:
        print 'not search' 
        sys.exit(1)

def get_reg():
    datas = get_DATA()
    print type(datas)
    for data in datas.split('\n'):
        if data:
            dic = get_result(data)
            print type(dic)
            msg = dic['msg']
            program = dic['program']
            hostname =dic['hostname']
            logtime = dic['logtime']
            conn_mysql(msg,program,hostname,logtime)
            
def conn_mysql(msg,program,hostname,logtime):
    try :
        conn = MySQLdb.connect(host='192.168.88.205',user='root',passwd='123456',port=3306)
        cur = conn.cursor()
        conn.select_db('python')
        cur.execute('insert into messages values(null,%s,%s,%s,%s)',(logtime,hostname,program,msg))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql error %d:%s" %(e.args[0],e.args[1])            
            
if __name__ == '__main__':
    print get_reg()





#mysql




#create tables  messages
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `logtime` varchar(50) DEFAULT NULL,
  `hostname` varchar(20) DEFAULT NULL,
  `program` varchar(20) DEFAULT NULL,
  `msg` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=585 DEFAULT CHARSET=utf8;
