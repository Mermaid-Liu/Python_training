# 编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
import time
user_status={'username':None,
    'status':False,
    'out_time':None}
def auth(type='file'):
    def wrapper(func):
        def inner(*args,**kwargs):
            if user_status['username']and user_status['status']:
                now=time.time()
                if now-user_status['out_time']<3:
                    res=func(*args,**kwargs)
                    return res
                else:
                    print("登录超时")
            else:
                if type=='file':
                    with open('log1','r',encoding='utf-8')as read_f:
                        dic=eval(read_f.read())
                        us=input("please input username>>")
                        pw=input("please input password>>")
                        if us in dic and pw==dic[us]:
                            user_status['name']=us
                            user_status['status']=True
                            user_status['out_time']=time.time()
                            res=func(*args,**kwargs)
                            return res
                        else:
                            print("wrong username or password")
                elif type=='mysql':
                    pass
                else:
                    pass
        return inner
    return wrapper;
@auth()
def excute():
    print("*******welcome********")
    time.sleep(3)
    print("yeah")
@auth()
def last():
    print("you have already login")
    time.sleep(2)
    print("yeah")
excute()
last()

