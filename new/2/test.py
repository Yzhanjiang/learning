#!/usr/bin/env python 
# coding:utf8

name = "yuanzhanjiang"
age = 10
print("hello " + name)
print("hello {0}".format(name))
print('hello %s' %name)
print("hello {0},my age is :{1}").format(name,age)

# tuple
str1 = "12sadfsfsfggasdasdcxcsaswdqafr244"
print(tuple(str1))
print(type(tuple(str1)))
a = ('a','b','c','abc','111')
print(a)

#但是使用tuple的时候要注意,单个tuple元素的时候，元素后面要加',',否则python
#解析器不会识别为tuple类型
m = ('a')
print(type(m))
n = ('abc',)
x = (123,)
print(type(n))
print(type(x))
#tuple方法:count index  不可变list
print(dir(x))
#count 统计某个元素的个数
tu1 = ('a','b','c','a','d','a','c')
print(tu1.count('a'))
#index  返回某个元素的下标
print(tu1.index('d'))
# print(tu1.index('dd'))  #不存在元素时报错


print('#'*30)
#字典
#1.字典的赋值方式
k = {'name':'zhan','age':20,'sex':'man'}
print(k)
print(type(k))
#list('addffgdf')  tuple('addasda')
k1 = dict(a=1,b=2,c=3)
print(k1)
#字典常用方法
d = dict([("name","zhan"),("age",20)])
print(d)

print(dir(d))
print(k.get('name'))
print(k.get('age'))

#setdefault
print(k.setdefault('age','beijing'))
print(k.setdefault('address','beijing'))
#keys
print(k)
print(k.keys())
print(k.iterkeys())

#values
print(k.values())
print(k.iteritems())
print(k.items())

for k1,v in k.iteritems():
    print(k1,v)

#pop
print(k)
print()
k.pop('address')
k.pop('sex')
print(k)



