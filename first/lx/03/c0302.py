目前只完成统计文件的小脚本。
#coding:UTF8
from optparse import  OptionParser

import os

import  sys 



def opt():

    parse = OptionParser()

    parse.add_option('-H',"--human",

                     dest='hm',

                     action="store_true",

                     default=False,

                     help=('print sizes in human readable format')

                     )

    options,args = parse.parse_args()

    return  options,args



def get_size(file):

    if os.path.isfile(file):

        hm = os.path.getsize(file)

        return hm 

    elif os.path.isdir(file):

        print " %s is dir,sorry Only support files "  %file

        return False

    else:

        print '%s not found!' %file

        return False

        

if __name__ =="__main__":

    options,args =opt()

    print options,args

    try:

        if len(args)==0:

            print "%s not follow argv" %__file__

            sys.exit()

        else:

            hm = get_size(args[0])

    except :

        sys.exit()

    if hm:

        k = hm/1024.0

        m =hm/(1024*1024.0)

        g =hm/(1024*1024*1024.0)



        if options.hm:

            flag = hm/1024.0

            if flag < 1:

                print  str(hm)+'B'

            elif flag >1 and flag <1024:

                print  str(k) + 'K'

            elif flag>1024 and flag <1024*1024:

                print  str(m) + 'M'

            else:

                print str(g)+'G'
