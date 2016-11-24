#coding:UTF8
import sys
from optparse import   OptionParser
import os

def opt():
    parse = OptionParser()
    parse.add_option('-a',"--append",
                     dest="append",
                     action="store_true",
                     default=False,
                     help=("append to the given FILEs, do not overwrite")
                     )
    parse.add_option('-w',"--writ",
                     dest="writ",
                     action="store_true",
                     default=False,
                     help=(" read from standard input and write to standard output and files")
                     )
    options,args = parse.parse_args()
    return  options, args

def get_file(file):
    if os.path.isfile(file):
        return file 
    elif os.path.isdir(file):
        print " %s is dir,sorry Only support files "  %file
        return False
    else:
        print '%s not found!,now create it' %file
        with open(file,'w') as fd:
            return file

def  file_append(filename):
    f = open(filename,'a')
    flag = 1
    while flag:
        try :
            a = raw_input()
            print '\033[1;31m%s\033[0m' %a
            print >> f,a
        except  EOFError:
            sys.exit()
    f.close()
def  file_write(filename):
    f = open(filename,'w')
    flag = 1
    while flag:
        try :
            a = raw_input()
            print '\033[1;31m%s\033[0m' %a
            print >> f,a
        except  EOFError:
            sys.exit()
    f.close()


if __name__ == "__main__":
    options,args = opt()
    print options,args
    try:
        if len(args)==0:
            print "%s not follow argv" %__file__
            sys.exit()
        else:
            filename = get_file(args[0])
            print filename
    except :
        sys.exit()
    if options.append:
        file_append(filename)
    else:
        file_write(filename)
    if options.writ:
        file_write(filename)
    
            

# who |python  tee.py  -a  /tmp/tee.log
# python  tee.py  -a /tmp/tee.log 
# cat 22.py  |python tee.py  -a /tmp/tee.log 
