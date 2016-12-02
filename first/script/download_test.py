#coding:utf-8
import urllib 
import threading
import urllib2 
import os
import time
import  sys 

#设置url
def get_url():
    #下载URL地址
    url = 'http://dldir1.qq.com/qqfile/qq/QQ8.7/19113/QQ8.7.exe'
    return url

#获取文件名称
def get_file_name(num):
    url = get_url()
    file_name= url.split('/')[-1] +"_" +str(num)
    return file_name

#下载文件
def get_file(num):
    url = get_url()
    print "downloading from  %s,  %s " %(url,time.ctime())
    file_name = get_file_name(num)
    urllib.urlretrieve(url, file_name)

#获取每秒下载文件大小    
def get_size(num):
    sum = 0 
    DIR = os.path.dirname(os.path.abspath(__file__))
    url = get_url()
    file_name = get_file_name(num)
    s1 = int(os.path.getsize(file_name))
    time.sleep(1)
    s2 = int(os.path.getsize(file_name))
    size = s2 - s1
    print   '''
            %s :%s KB/S
            ''' %(os.path.join(DIR,file_name) ,size/1024.0)
    return size/1024.0

if __name__ =="__main__":
    #tt 显示下载文件时间
    tt = 60
    DIR = os.path.dirname(os.path.abspath(__file__))
    print "Directory:" + DIR
    try :
#         argv = sys.argv[1]
        argv = 5
    except IndexError:
        print "%s follow a number" %__file__
        sys.exit()
    
    for i in xrange(int(argv)):
#     for i in xrange(15):
        t = threading.Thread(target=get_file,args=(i,))
        t.start()
    time.sleep(2) 
    while tt:
        for i in xrange(int(argv)):
        #for i in xrange(15):
            t2= threading.Thread(target=get_size,args=(i,))
            t2.start()    
        print "*****************"
        time.sleep(1)
        tt  -=1
