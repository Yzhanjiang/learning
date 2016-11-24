#coding:UTF8
#找出目录中占用空间大的前10个文件。
import sys
import  os
import  operator

def get_size(file):
    size = os.path.getsize(file)
    return  size
def get_dic(path):
    a = os.walk(path)
    dic = {}
    dic1 = {}
    for p,d,f in a :
        for i in f:
            f =  os.path.join(p,i)
            s = get_size(f)
            dic1[f]= s
            dic.update(dic1)
    return dic

def main():
    try :
        dirs = sys.argv[1]
        if  len(sys.argv) == 0:
            print "%s need follow  argument"  % __file__
        else:    
            if os.path.isdir(dirs):
                dic = get_dic(sys.argv[1])
            else:
                print "%s need follow  directory"  % __file__
                sys.exit()
    except :
        print "No such file or directory"  
        sys.exit()
    sorted_dic = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)
    for k,v in sorted_dic[:10]:
        print v,  k

if __name__ == '__main__':
    main()
