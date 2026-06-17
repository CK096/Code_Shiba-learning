#Python 中的模组 Module
import math
#help(math) #help()寻找所有的模组用法

x = 20.6
print(math.ceil(x))
print(math.floor(x))
print(math.pi)
print(math.pow(2,3))


import math as m #可以缩写用的模组

y = 20.6
print(m.ceil(y))
print(m.floor(y))
print(m.pi)
print(m.pow(2,6))

from math import pi #这样可以直接使用模组里面单个东西
print(pi)

import module_intro_test as lol #可以做自己的模组使用
print(lol.B)
print(lol.square(6))
print(lol.cube(3))
print(lol.area(5))