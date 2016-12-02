#coding:utf8
# dir cat 1.txt |grep 'sucess'

import os
from subprocess import Popen,PIPE
import re 

def get_dirs():
    # DIR = R'/data/logs/app.huaguogou.com'
    DIR = r'E:\20161202'
#     DIR = r'/mnt/hgfs/workspace/'
    
    dirs = os.listdir(DIR)
    L = []
    for i in dirs:
        file = os.path.join(DIR,i)
        if os.path.isdir(file):
            L.append(file)
    return L

# def read_file(cmd):
#     p =Popen(cmd,stdout=PIPE,shell=True)
#     data = p.stdout.read()
#     return data 
    
def re_1(data):
    re1 = re.compile(r"ShaoKe_service")
    a = re1.search(data)
    if  a :
        return data      

def writ_log(context):
        with open(r'dl.log','a+') as fd:
            fd.write(context)

def get_file_cont(file_name):
    L = get_dirs()
#     print L
    for file_name in L:
        print file_name
        file_name = os.path.join(file_name,"app_access.log")
        if os.path.isfile(file_name):
            #file_name = "/mnt/hgfs/workspace/LX/app_access.log"
            print file_name
            with open(file_name,'r') as  fd:
                while True:
                    data = fd.readline()
                    if data:
                        read1 =  re_1(data)
                        if read1 :
#                             print read1,file_name + '\n'
                            context = '''%s,%s  \n
                                    ''' %(read1,file_name)
                            print context
                            writ_log(context)
#                             return  read1,file_name
                
                
if __name__ == "__main__":
    dir = get_dirs()
    data = get_file_cont(dir)
    print data 
