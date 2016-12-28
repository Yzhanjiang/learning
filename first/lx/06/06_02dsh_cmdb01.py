1. 自己安装一个clusterit软件包，产生一个dsh命令，用来实现并行命令。

安装clusterit软件包，产生一个dsh命令。服务器间通过免密钥访问

dsh -w 192.168.88.205 uptime

192.168.88.205:  16:28:22 up  6:42,  3 users,  load average: 0.05, 0.03, 0.00



2. 根据自己的cmdb实现并行命令





#coding:UTF8

import  threading

import sys 

import multiprocessing 

from optparse import  OptionParser

import urllib,urllib2

from subprocess import   Popen,PIPE

import  json

import  shlex

import   time

from IPython.utils.io import stdout



DATA_BACK = '/var/tmp/data.json'



def opt():

    parser = OptionParser("Usage: %prog -a|-g command")

    parser.add_option('-a',

                      dest='addr',

                      action='store',

                      help='ip or iprange EX:192.168.1.3 or 192.168.1.1-192.168.1.100')

    parser.add_option('-g',

                      dest='group',

                      action='store',

                      help='groupname')

    options ,args = parser.parse_args()

    return options,args



def  parseOpt(option):

    if ',' in option:

        ips = option.split(',')

        return ips

    elif '-' in option:

        ip_start,ip_end = option.split('-')

        ip_net = '.'.join(ip_start.split('.')[:-1])

        start = int(ip_start.split('.')[-1])

        end = int(ip_end.split('.')[-1]) + 1

        ips = [ip_net +'.'+str(i) for i in range(start,end)]

        return ips

    elif ',' not in option  or '-' not in option:

        ips = [option]

        return ips 

    else:

        print "%s -h" % __file__

    

def getData():

    url = 'http://192.168.88.216:10001/hostinfo/getjson/'

    try:

        req = urllib2.urlopen(url)

        data = json.loads(req.read())

        with open(DATA_BACK,'wb') as fd:

            json.dump(data,fd)

    except:

        with open(DATA_BACK) as fd:

            data = json.load(fd)

    return data 

    

def parseData(data):

    dic_host = {}

    for hg in data:

        groupname = hg['groupname']

        dic_host[groupname] = []

        for h in hg['members']:

            dic_host[groupname] += [h['ip']] 

    return dic_host



def get_result(ip,cmd):

    cmd = 'dsh -w' +' '+str(ip)+' '+str(cmd)

    p = Popen(shlex.split(cmd),stdout=PIPE,stderr=PIPE)

    stdout,stderr = p.communicate()

    if stdout:

        print "%s: \t %s" %(ip,stdout)

    else:

        print "%s:\t %s" % (ip,stderr)



if __name__ == '__main__':

    options,args = opt()

    try:

        cmd = sys.argv[-1]

    except IndexError:

        print "%s follow a command" % __file__

        sys.exit(1)

    if  options.addr:  

        ips = parseOpt(options.addr)

    elif options.group:

        groupname = options.group

        data = getData()

        dic = parseData(data)

        if groupname in dic:

            ips = dic[groupname]

        else:

            print "%s is not exists in SimpleCMDB" % groupname 

    else:

        print "%s -h" % __file__

        sys.exit()

    pool = multiprocessing.Pool(processes=5)   

    print ips

    for ip in ips: 

#         t = threading.Thread(target=get_result,args=(ip,cmd,))

#         t.start()

        pool.apply_async(func=get_result,args=(ip,cmd))

    pool.close()

    pool.join()


 python  dsh_cmdb.py  -a 192.168.88.205,192.168.88.202  uptime

['192.168.88.205', '192.168.88.202']

dsh -w 192.168.88.205 uptime

dsh -w 192.168.88.202 uptime

192.168.88.205:          192.168.88.205:  16:29:49 up  6:43,  3 users,  load average: 0.01, 0.02, 0.00



192.168.88.202:          192.168.88.202:  16:29:49 up  6:38,  2 users,  load average: 0.00, 0.01, 0.05



[root@zhan 20]# python  dsh_cmdb.py  -g db  uptime

[u'192.168.88.205']

dsh -w 192.168.88.205 uptime

192.168.88.205:          192.168.88.205:  16:30:01 up  6:44,  3 users,  load average: 0.01, 0.02, 0.00
