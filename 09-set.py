# 集合（Set）是简单对象的无序集合（Collection）。当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就会使用集合。
# 通过使用集合，你可以测试某些对象的资格或情况，检查它们是否是其它集合的子集，找到两个集合的交集，等等。

# 集合的特征
# 1.集合是一种无序的数据类型，无法通过索引和分片进行操作
# 2.集合是内部元素绝对唯一的数据，常常用于去掉重复数据
# 3.集合的数据，str，int，float,bool,tuple，冰冻集合。
'''
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True
>>> 'usa' in bri
False
>>> bric = bri.copy()
>>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
'''


#1
