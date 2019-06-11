#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-10 15:44
# @Author  : Mermaid  
# @File    : Item_shopping.py
# 需求:
#     用户名，密码和余额存放于文件中，格式为：Albert|Albert123|3000
# #     启动程序后：
# #         已注册用户===>先登录===>登录成功===>读取用户余额===>开始购物
# #                      登录过程中，用户密码输入超过三次则退出程序,
# #                      并将用户名添加到黑名单，再次启动程序登陆改用户名，提示用户禁止登陆
# #         未注册用户===>先注册===>注册成功===>输入用户工资，即为用户余额===>开始购物
# #                      注册过程中，用户密码输入两次一样才可以注册
# #     允许用户根据商品编号购买商品，比如：
# #         1 iPhone
# #         2 macbook
# #         3 bike
# #     用户选择商品后，检测余额是否够，够就直接扣款，修改文件中用户余额，不够就提醒
# #     可随时退出，退出时，打印已购买商品和余额

#读取文件将字符串拆分
f = open(r'userInfo',mode='r',encoding='utf-8')
data=f.read();
f.close();
print(data)
user_list=data.split('\n')
print(user_list)
product_name = ['iPhone', 'iPad', 'mac book']
dict_product = dict([['1',4999], ['2',2999], ['3',8999]])
b_list=[]
def login():
    tag=True;
    while tag:
        user_new=str((input("请输入你的用户名>>")))
        psd_new = str((input("请输入你的密码>>")))
        psd_verify= str((input("请再次输入你的密码>>")))
        if psd_new==psd_verify:
            print("开始花钱吧")
            rest_info=str(input("请输入你的工资>>"))
            user_new='|'.join([user_new,psd_new,rest_info])
            print(user_new)
            print(user_list)
            user_list.append(user_new)
            print(user_list);
            tag=False
        else:
            print("两次输入的密码不一致，请重新输入")
def signIn():
    tag=True;
    n=0;
    while tag:
        user=str(input("请输入你的用户名"))
        password=str(input("请输入你的密码"))
        verified='|'.join([user,password])
        if verified in b_list:
            print("当前请求被拒绝")
            break;
        dict_info=dict([info.rsplit('|', 1)for info in user_list])
        if verified in list(dict_info.keys()):
            print("登录中")
            rest = dict_info[verified]
            print(rest);
            break
        elif n<2:
            print("你的信息不存在，请重新输入")
        n+=1;
        if n==3:
            print("你的用户名不存在")
            b_list.append(verified);
            break;
    return rest

#main
first_look=input("你是新来的么？y/n")
if first_look=='y':
    login();
    rest=int(signIn())
    print(rest)
if first_look=='n':
    rest=int(signIn())
print("我们所售卖的产品清单有：")
for k,v in enumerate(product_name,1):
    print(k,v)
selected=input("请输入你所想要的产品的编号")
price=int(dict_product[selected])
print("价格是",price)
if rest < price:
    print('啊哦，你的钱不够!')
else:
    rest = rest - price
    print('你的余额为',rest)

