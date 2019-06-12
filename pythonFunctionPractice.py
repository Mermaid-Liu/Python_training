# 写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
import os
def modify_file(name,content,newstr):
    new_file_name='%name'%'new.'
    f_new=open(new_file_name,'w')
    if os.path.exists(name):
        with open(name,'r+')as f:
            for line in f:
                if content in line:
                    line=line.replace(content,newstr)
                f_new.close();
                os.rename(new_file_name,name)
    else:
        exit('file is not exist')
# 写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def cal_number(p_obj):
    alpha_num=0;
    digit_num=0;
    space_num=0;
    others_num=0;
    for item in p_obj:

        if item.isdigit():
            digit_num+=1
        elif item.isspace():
            space_num+=1
        elif item.isalpha():
            alpha_num+=1
        else:
            others_num+=1
        return(alpha_num,digit_num,space_num,others_num)
p=cal_number("asd123 adsfju!")
print(p)
# 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def func_length(obj):
    if len(obj)>5:
        return True
    else:
        return False
content=input("请输入你要检测的内容")
print(func_length(content))
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def func_length2(input_array):
    if len(input_array)>2:
       del input_array[2:]
q=[12,14,15,16]
func_length2(q)
print(q)
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def app_func(old_arg):
    new_arg=[]
    new_arg.append(old_arg[1::2])
    print(new_arg)
    return new_arg
o=[1,2,3,6,5,4,7,8,9,45]
print(app_func(o))
# 写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def check_length(dics):
    ret={}
    for key,value in arg.items():
        if len(value)>2:
            ret[key]=value[0:2]
        else:
            ret[key]=value
    return ret

dic={"k1":"v1","k2":[11,12,13]}
r=check_length(dic)
print(r)
