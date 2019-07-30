# 程序设计，自定义轿车元类CarMeta，实现元类为CarMeta的类至少有生产日期(production_date)、
# 发动机编号(engine_number)及载客量(capacity)三个基本属性，没有就不行
class CarMeta(type):
    def __call__(self, *args, **kwargs):
        print(args)
        if len(args)<3:
            raise ValueError(" ")
        obj=object.__new__(self)
        self.__init__(obj,*args,**kwargs)

        if not ("production_date" in obj.__dict__ and"engine_number" in obj.__dict__ and"capacity"in obj.__dict__):
            raise ValueError(" ")
        return obj
class BigCar:
    def __init__(self,production_date,engine_number,capacity):
        self.production_date=production_date
        self.engine_number=engine_number
        self.capacity=capacity
car=BigCar("20180730","101101",6)
print(car)
