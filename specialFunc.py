#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 06:48
# @Author  : Mermaid  
# @File    : specialFunc.py
# 要求从文件中取出每一条记录放入列表中,列表的每个元素都是如下格式：
# {'name':'albert','sex':'male','age':18,'salary':3000}
with open('log1.txt',encoding='utf-8')as f:
    info=[{
        'name':line.split()[0],
        'sex':line.split()[1],
        'age':line.split()[2],
        'salary':line.split()[3]
    }for line in f ]
print(info)
# 根据题目1得到的列表,取出薪资最高的人的信息
print(max(info,key=lambda dic:dic['salary']))
# 根据题目1得到的列表,取出最年轻的人的信息
print(min(info,key=lambda dic:dic['age']))
# 根据题目1得到的列表,将每个人的信息中的名字映射成首字母大写的形式
info_new=map(lambda item:{'name':item['name'].capitalize(),
                          'sex':item['sex'],
                          'age':item['age'],
                          'salary':item['salary']},info)

print(list(info_new))
# 根据题目1得到的列表,过滤掉名字以a开头的人的信息
g=filter(lambda item:item['name'].startswith('a'),info)
print(list(g))
#使用递归打印斐波那契数列(前两个数的和得到第三个数，如：0 1 1 2 3 4 7...)
def fib(a,b,stop):
    if a>stop:
        return
    print(a,end='')
    fib(b,a+b,stop)
fib(0,1,10)
#l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]
l=[1,2,[3,[4,5,6,[7,8,[9,10,[11,12,13,[14,15]]]]]]]
def get(seq):
    for item in seq:
        if type(item)is list:
            get(item)
        else:
            print(item)
get(l)
