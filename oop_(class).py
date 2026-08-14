# Python 物件导向设计 OOP

# 物件(Object)是类别(Class)的实例(Instance)

#例子
# 车 = 类别 (class)
#每一台生产的车子 = 物件 (Object)

class Car:
    def __init__(self,make,model,year,color):
        #初始化
        self.make_by = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(self.model + "is Driving")

    def stop(self):
        print(self.model + " is Stop")

car1 = Car("Toyota","Altis",2021,"Blue")
car2 = Car("Ford","Kuga",2020,"White")
print(car2.make_by)
print(car2.model)
print(car2.year)
print(car2.color)

car1.stop()