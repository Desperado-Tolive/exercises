import keyword
# 查看系统关键字，关键字不可做变量的命名
print(keyword.kwlist)


import math
# ceil(x) => integer    向上取整，返回整型
print(math.ceil(5.1))

# floor(x) => integer   向下取整，返回整型
print(math.floor(5.1))

# round(number[, ndigits]) -> number   四舍五入，内置函数，返回整型
print(round(5.1))
print(round(5.5))

# sqrt(x) => float   开平方，返回浮点数
print(math.sqrt(4))

# pow(x,y) => float  X的N次幂，返回浮点数
print(math.pow(4,3))
# 幂运算   返回整型
print(4**3)

# fabs(x) => float   计算一个数的绝对值，返回浮点数
print(math.fabs(-1.5))
print(math.fabs(3))
print(math.fabs(0))

# abs(*args, **kwargs)  计算一个数的绝对值，内置函数，返回原类型
a = 0
print(abs(-1.5))
print(abs(3))
print(abs(a))

# fsum(iterable) => float   对整个序列求和，返回浮点数
print(math.fsum([1,2,3,4,5]))
print(math.fsum({1,2,3,4,5}))

# sum(*args, **kwargs)  求和，返回原类型，内置函数
a = 4
print(sum([1,2,3,4,5.2],a))
'''
Union在C++表示联合体，_S表示结构体，_T表示一个类型
'''

# modf(x) => Tuple[float,float]     将一个浮点数拆分为小数部分和整数部分组成的元组，返回元组
print(math.modf(2.5))

# copysign(x, y)    返回一个带有x的大小（绝对值）的浮点数，但是符号是y的，即把y正负号传给x的绝对值（浮点数）并返回结果
print(math.copysign(2,-3))  # -2.0
print(math.copysign(-2,-3)) # -2.0

# Variables with simple values  可直接调用，如下
'''
e = 2.718281828459045

inf = inf

nan = nan

pi = 3.141592653589793

tau = 6.283185307179586
'''
print(math.e)
print(math.inf)
print(math.pi)


import random
# random(self)  返回[0,1)之间的随机小数
for i in range(10):
    print(random.random())

# randint(self, a, b)   返回[a, b]之间的随机整数，a和b必须是 如 1或1.0
for i in range(10):
    print(random.randint(0.0,10))
print()

# randrange(start, stop[, step])    返回[a,b)之间的随机数，步数默认为1可指定，只能填整数，非整数报错
# 函数定义是def randrange(self, start, stop=None, step=1, _int=int):
'''
领悟（此时还未看源码）：
说明，self获取函数自身的参数（目前所学还不能肯定）
if stop=None:   # 即调用时不填stop，randrange(start)
    获取range(start)内的随机数 # 或者函数内的方法可能是直接令 stop = start
else:           # 此时调用时填了stop，randrange(start，stop[, step])
    获取range(start,stop)内的随机数
    
还可使用这种方法调用：    # 联想到关于位置参数和关键字参数的知识
random.randrange(stop=10,start=0,step=2)
random.randrange(start,step=2)  # 若stop = None时还需要用到步数那么只能step只能使用关键字参数调用

_int=int 用于强制转换，这句命令完成了赋值，即此时 _int(1.1) == int(1.1)
'''
for i in range(10):
    print(random.randrange(1,10,2))
print()

# choice(non-empty sequence)    随机获取序列中的元素
for i in range(10):
    print(random.choice([1,3,'a']))
print()

# shuffle(self, x, random=None) 随机打乱列表，无返回值
l = [1,2,3,4,5,6,7]
random.shuffle(l)
print(l)
print()

# uniform(self, a, b)   在[a,b)或[a,b]之间获取一个随机数（整数或浮点数）
print(random.uniform(0,10))