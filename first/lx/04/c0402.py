# python里执行dmidecode命令，并保存到文件

#coding:utf8
from  subprocess import Popen,PIPE
import os
import  sys
def getdmi():
    p=Popen(['dmidecode'],stdin=PIPE,stdout=PIPE,stderr=PIPE)
    data = p.stdout
    L=[]
    while True:
        line = data.readline()
        if line:
    #         print line,
            L.append(line)
        else:
            break
    return L


def write_dmi(file):
    L=getdmi()
    with open(file,'w') as fd:
        for i in L:
            fd.write(i)

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
    write_dmi(file)
