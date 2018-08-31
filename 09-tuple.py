# 元组不可修改，因此相比列表只有count和index两个函数
#1 T.count(value) -> integer    计算指定值在L中出现的次数，返回整型  //与S.count()不同的是，T.count()是全文搜索，不能指定起始
t = (1,1,3,3,2,2,3)
print(t.count(3))

#2 T.index(value, [start, [stop]]) -> integer   查找T中是否具有指定的值，返回第一次出现的索引，查找不到直接报错
print(t.index(3))