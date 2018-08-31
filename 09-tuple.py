# 元组（Tuple）用于将多个对象保存到一起。你可以将它们近似地看作列表，但是元组不能提供列表类能够提供给你的广泛的功能。元组的一大特征类似于字符串，它们是不可变的，也就是说，你不能编辑或更改元组。
# 元组是通过特别指定项目来定义的，在指定项目时，你可以给它们加上括号，并在括号内部用逗号进行分隔。
# 元组通常用于保证某一语句或某一用户定义的函数可以安全地采用一组数值，意即元组内的数值不会改变。
# 包含0或1个项目的元组：一个空的元组由一对圆括号构成，就像 myempty = () 这样。然而，一个只拥有一个项目的元组并不像这样简单。你必须在第一个（也是唯一一个）项目的后面加上一个逗号来指定它，如此一来 Python 才可以识别出在这个表达式想表达的究竟是一个元组还是只是一个被括号所环绕的对象，也就是说，如果你想指定一个包含项目 2 的元组，你必须指定 singleton = (2, )。
# 定义一个参数时若有多个元素且没有加括号，那么默认这个参数是元组，如 t = 'a','b'，type(t) == <class 'tuple'>
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2]) # 这里的调用类似二元数组
print('Number of animals in the new zoo is',
    len(new_zoo)-1+len(new_zoo[2]))


# 元组不可修改，因此只有count和index两个函数

#1 T.count(value) -> integer    计算指定值在L中出现的次数，返回整型  //与S.count()不同的是，T.count()是全文搜索，不能指定起始
t = (1,1,3,3,2,2,3)
print(t.count(3))

#2 T.index(value, [start, [stop]]) -> integer   查找T中是否具有指定的值，返回第一次出现的索引，查找不到直接报错
print(t.index(3))