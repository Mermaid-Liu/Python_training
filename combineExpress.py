# 将names=['albert','james','kobe','kd']中的名字全部变大写
names=['albert','james','kobe','kd']
names=[name.upper() for name in names]
print(names)

# 将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names=['albert','jr_shenjing','kobe','kd']
names=[len(name) for name in names if not name.endswith('shenjing')]
print(names)

# 求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）
with open('log.txt',encoding='utf-8')as file:
    print(max(len(line) for line in file))

# 文件shopping.txt内容如下，分别代表商品，价格和数量
# （1）求总共花了多少钱？
# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
# （3）求单价大于10000的商品信息,格式同上
file=open('log.txt',encoding='utf-8')
sum=0;
for line in file.readlines():
    # print(line);
    line=line.strip().split(" ")
    # print(line)
    a=line[1]
    # print(type(a))
    sum=sum+int(line[1]*int(line[2]))
print(sum)#总价格
with open('log.txt',encoding='utf-8')as f:
    info=[{
              'name':line.split()[0],
                'price':float(line.split()[1]),
                'count':int(line.split()[2])
    } for line in f]
print(info)
f.close()

with open('log.txt',encoding='utf-8')as f:
    info=[{
        'name':line.split()[0],
        'price':float(line.split()[1]),
        'count':int(line.split()[2])
    } for line in f if float(line.split()[1])>10000]
    print(info)
f.close()
