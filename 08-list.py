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

#9 L.remove(value) -> None  删除列表中第一次出现的指定的值的元素，无返回值 //原地删除   项——对象——值   索引——元素（起始为0）
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
