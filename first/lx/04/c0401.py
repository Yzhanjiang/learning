#coding:UTF8
#写一个程序显示文件内容，要求：
#程序带一个参数，如果没有带参数提示并退出，如果文件不存在提示退出，如果不是标准文件提示退出，使用异常处理。
import sys
import os

def get_file(f):
    if len(f)==0:
        print '%s follow argv' %__file__
        sys.exit()
    else:
        if os.path.isfile(f):
            return  f
        else:
            print "%s not file" % f
             
def get_content(file):
    try:
        with open(file,'r') as fd :
            while True:
                data = fd.read(1024)
                if data :
                    print data
                else:
                    break
    except TypeError:
        print "coercing to Unicode: need string or buffer, NoneType found"
        sys.exit()


if __name__ == '__main__':
    f = get_file(r'D:\samcoins.dll')
#     f = get_file(r'D:\php.ini')
    get_content(f)
