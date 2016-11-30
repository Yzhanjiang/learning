#coding:UTF8

from subprocess import Popen,PIPE
import time
import  sys 
import os 

def  get_data():
    # p = Popen('ping 192.168.88.1 -n 10',stdin=PIPE,stdout=PIPE,shell=True)
    p = Popen('tcpdump -c1000 -nn -i br0 port 68 -l',stdin=PIPE,stdout=PIPE,stderr=PIPE,shell=True)
    data = p.stdout
    return data 

def write_file(file,lines):
    with open(file,'a') as fd:
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        fd.write(lines + '  '+ t +'\n')
                   
def get_mac(file):
    lines = []
    data = get_data()
    while True:
        line = data.readline()
        if line:
            new_line=line.split(',')[1].strip()
            if new_line.startswith('Request'):
                new = new_line.split()[2]
#                 lines.append(new)
                print(new)
                write_file(file,new)
        else:
            break
    
if __name__ == '__main__':
    try:
        file=sys.argv[1]
        if os.path.isdir(file):
            print "%s Is a directory" %file
            sys.exit()
        else:
            pass
    except:
        print "%s follow file" %__file__
        sys.exit()
    get_mac(file)


#python  get_mac.py   mac.txt
