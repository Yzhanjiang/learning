#coding:utf-8
# 写一个四则运算器，要求从键盘读取数字

import  sys 
def is_Number(number):
    while True:
        num = raw_input('please input %s :' %number)  
        if num.isdigit():
            print "%s is: %s" %(number,num)
            return int(num)
        else :
            print "%s is not a number" %num
           
def yunS(aa,num1,num2):
    if aa == "+":
        print "%d + %d = %d "  %(num1,num2,(num1 + num2))
    elif aa == "-":
        print "%d - %d = %d "  %(num1,num2,(num1 - num2))
    elif aa == "*":
        print "%d * %d = %d "  %(num1,num2,(num1 * num2))
    elif aa == "/":
        try:
            print "%d / %d = %.2f "  %(num1,num2,(float(num1) / num2))
        except ZeroDivisionError:
            print "integer division or modulo by zero"
            print "除数不能为0"
    elif aa=="q" or aa =="Q":
        print "请从新输入2个数字!!!"
    else:
        print "输入错误！！！"
        
def main():                 
    nn = True
    while nn:
        num1 = is_Number("num1")
        num2 = is_Number("num2")
        print "1、加法运算:+"
        print "2、加法运算:-"
        print "3、加法运算:*"
        print "4、加法运算:/"
        print "5、退出程序:exit"
        aa = raw_input("请选择需要进行的运算( + - * /   [退出本次计算:q or Q]):")
        if aa == "exit":
            sys.exit()
        else:
            yunS(aa,num1,num2)
if __name__ == '__main__':
    main()
    
    
    
    
    
    

        
        
    
    
