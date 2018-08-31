# 数据结构（Data Structures）基本上人如其名——它们只是一种结构，能够将一些数据聚合在一起。换句话说，它们是用来存储一系列相关数据的集合。
# Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集合（Set）。我们将了解如何使用它们，并利用它们将我们的编程之路变得更加简单。


# 列表是一种用于保存一系列有序项目的集合，也就是说，你可以利用列表保存一串项目的序列。想象起来也不难，你可以想象你有一张购物清单，上面列出了需要购买的商品，除开在购物清单上你可能为每件物品都单独列一行，在 Python 中你需要在它们之间多加上一个逗号。
# 项目的列表应该用方括号括起来，这样 Python 才能理解到你正在指定一张列表。一旦你创建了一张列表，你可以添加、移除或搜索列表中的项目。既然我们可以添加或删除项目，我们会说列表是一种可变的（Mutable）数据类型，意即，这种类型是可以被改变的。
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

#1 L.append(object) -> None 追加对象到末尾，无返回值 //原地追加 （即在原有列表追加，还是原来的地址）
l = [1,2,10,3,4,5]
print(id(l))
l.append(6)
print(l)
print(id(l))
print()

#2 L.clear() -> None    清空列表，无返回值 //原地删除
l.clear()
print(l)
print()
'''
顿悟：help文档里的list代表类，L则代表list类的变量
'''

#3 L.copy() -> list 浅拷贝L，返回list //浅拷贝：复制值到一个新的地址。也就是说浅拷贝不是传址而是传值，l2 = l1.copy() 同等与 l2 = [l1]
l1 = [1,3,5,7,9]
l2 = l1
print(id(l1))   # 2971727466120
print(id(l2))   # 2971727466120
l1.append(11)   # 此处改变了list的值
print(l1)       # [1, 3, 5, 7, 9, 11]
print(l2)       # [1, 3, 5, 7, 9, 11]
print(id(l1))   # 2971727466120
print(id(l2))   # 2971727466120
print()         # 以上完美说明list类 l2 = l1 是传址操作，同时说明了L.append(object)是原地追加

l2 = l1.copy()  # 传值
print(id(l1))   # 2971727466120
print(id(l2))   # 2971727466120
print()         # 说明L.copy()是传值操作，浅拷贝

# 测试
num1 = 5
num2 = 5
print(id(num1)) # 1735814752
print(id(num2)) # 1735814752
str1 = "5"
str2 = "5"
print(id(str1)) # 2469641122232
print(id(str2)) # 2469641122232
l1 = [5]
l2 = [5]
print(id(l1))   # 2469641153224
print(id(l2))   # 2469641152712
print()
'''
以上说明n = num/s = "str"/l = [list]均是传值操作
因为Python会保留常用的值不会销毁，int类-5--256时，id(num1)==id(num2)，在这范围外id(num1)!==id(num2)
'''

#4 L.count(value) -> integer    计算指定值在L中出现的次数，返回整型  //与S.count()不同的是，L.count()是全文搜索，不能指定起始
l = [1,3,3,3,1,2,3]
print(l.count(3))
print()

#5 L.extend(iterable) -> None   追加新的序列在L最后，无返回值 //原地追加 （即在原有列表追加，还是原来的地址）
l1 = [1,2,3,4]
l2 = [5,6,7]
l1.extend(l2)   # [1, 2, 3, 4, 5, 6, 7]
print(l1)
print()

#6 L.index(value, [start, [stop]]) -> integer   查找L中是否具有指定的值，返回第一次出现的索引，查找不到直接报错
l = [1,2,3,4,5]
print(l.index(5,0,5))   # 4 [start, [stop]]含左不含右
print()

#7 L.insert(index, object) -> None  在索引前插入对象，无返回值 //原地插入
l = [1,2,3,4,5]
l.insert(3,0)
print(l)
print()

#8 L.pop([index]) -> item   取出一个元素，默认取出最后一个，返回取出项   //原地删除   项——对象——值   索引——元素（起始为0）
l = [1,2,3,4,5]
print(l.pop())
print(l)
print(l.pop(1))
print(l)
print()

#9 L.remove(value) -> None  删除列表中第一次出现的指定的值的元素，无返回值，找不到报错 //原地删除   项——对象——值   索引——元素（起始为0）
l = [1,2,3,1,2,3]
l.remove(1)
print(l)
print()

#10 L.reverse() -> None 反转列表，无返回值   //原地反转
l = [1,2,3,4,5]
l.reverse()
print(l)
print()

#11 L.sort(key=None, reverse=False) -> None 排序，默认正序，若要倒序则加参数reverse=True，无返回值    //原地排序
l = [6,2,8,4,0]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
