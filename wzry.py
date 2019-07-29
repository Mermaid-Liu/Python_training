# 简易王者荣耀
# 1.设计王者荣耀中的英雄类,每个英雄对象可以对其他英雄对象使用技能
# 2.英雄具备以下属性英雄名称,等级,血量和Q_hurt,W_hurt,E_hurt 三个伤害属性,表示各技能的伤害量
# 3.具备以下技能Q W E三个技能都需要一个敌方英雄作为参数,当敌方血量小于等于0时输出角色死亡

class Hero(object):
    def __init__(self,name='',rank='',blood='',Q_hurt='',W_hurt='',E_hurt='' ):
        self.name=name;
        self.rank=rank;
        self.blood=blood;
        self.Q_hurt=Q_hurt;
        self.W_hurt=W_hurt;
        self.E_hurt=E_hurt;

    def bite(self,enemy):
        enemy.blood-=(self.Q_hurt+self.W_hurt+self.E_hurt)
        print('''英雄[%s]打了英雄[%s]
        英雄[%s]掉了[%s]
        英雄[%s]还剩血量[%s]'''
              %(self.name,enemy.name,enemy.name,(self.Q_hurt+self.W_hurt+self.E_hurt),enemy.name,enemy.blood))
h1 = Hero('露可娜娜',12,300,12,34,56)
h2 = Hero('鲁班',12,200,12,34,54)
h1.bite(h2)
