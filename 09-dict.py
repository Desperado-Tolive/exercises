# 字典就像一本地址簿，如果你知道了他或她的姓名，你就可以在这里找到其地址或是能够联系上对方的更多详细信息，换言之，我们将键值（Keys）（即姓名）与值（Values）（即地址等详细信息）联立到一起。在这里要注意到键值必须是唯一的，正如在现实中面对两个完全同名的人你没办法找出有关他们的正确信息。
# 另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可变或不可变的对象作为字典中的值。基本上这段话也可以翻译为你只能使用简单对象作为键值。
# 在字典中，你可以通过使用符号构成 d = {key : value1 , key2 : value2} 这样的形式，来成对地指定键值与值。在这里要注意到成对的键值与值之间使用冒号分隔，而每一对键值与值则使用逗号进行区分，它们全都由一对花括号括起。
# 另外需要记住，字典中的成对的键值—值配对不会以任何方式进行排序。如果你希望为它们安排一个特别的次序，只能在使用它们之前自行进行排序。
# 字典是一种组合数据，没有顺序的组合数据。数据以键值对的方式存在。

#字典的定义
'''
1.创建空字典

变量 = {} 或者 变量 = dict()

2.创建有数据的字典

1.变量 = {键:值,键:值,键:值...}

2.变量 = dict({键:值,键:值,键:值...})

3.变量 = dict(键=值,键=值,键=值...)

    注意：该方法键的名称要符合变量的基本名规则

4.变量 = dict([(键,值),(键,值),（键,值）...])

5.变量 = dict(zip((键，键，键....),(值,值，值...)))
'''

# 案例
ab = {                                  # “ab”是地址（Address）簿（Book）的缩写
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])
del ab['Spammer']       # 删除一对键值—值配对
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))     # 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

# 阅读下面的代码，写出A0，A1至An的最终值。
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]     # []
A3 = [A0[s] for s in A0]            # [1,2,3,4,5]
A4 = [i for i in A1 if i in A3]     # [1,2,3,4,5]
A5 = {i:i*i for i in A1}            # {0:0,1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81}
A6 = [[i,i*i] for i in A1]          # [[0,0],[1,1],[2,4]...]

# 下面代码会输出什么：

def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)            # l = [0, 1]
f(3,[3,2,1])    # l = [3, 2, 1, 0, 1, 4]
f(3)            # l = [0, 1, 0, 1, 4]


#1 D.clear() -> None    清空字典，无返回值 //原地删除
d = {1:'a',2:'b'}
d.clear()
print(d)

#2 D.copy() -> a shallow copy of D  浅拷贝字典，返回字典
d1 = {1:'a',2:'b'}
d2 = d1.copy()
print(d2)