#coding:UTF8
#字典排序
#统计目录下占用空间最大的前10个文件
import  os
import sys
import  operator

def get_dic(topdir):
    dic = {}
    a = os.walk(topdir)
    for p,d,f in a :
        for i in f:
            fn = os.path.join(p,i)
            f_size = os.path.getsize(fn)
            dic[fn]=f_size
    return dic 

if __name__ =='__main__':
    dic = get_dic(sys.argv[1])
    sorted_dic = sorted(dic.iteritems(),key=operator.itemgetter(1),reverse=True)
    for k,v in sorted_dic[:10]:
        print k,v 
