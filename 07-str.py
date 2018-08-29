# 切片
s = "123456789"
s1 = s[:]
print(type(s1)) # type依然是S
print(s)
print(s1)
print(id(s))
print(id(s1))
print()         # s与s1的id相同，S字符串完整切片s[:]并没有进行任何操作

s1 = s[:6]
s2 = s[:6]
print(s1)
print(s2)
print(id(s1))
print(id(s2))
print()         # s1与s2的id不同，S字符串部分切片s[:6]是创建出要切片的部分，因此每次切片地址不同，是独立的

s1 = s[:1]
s2 = s[:1]
print(s[0])
print(s1)
print(s2)
print(id(s[0]))
print(id(s1))
print(id(s2))
print()         # s[0]和s1的id相同，S字符串切片只有一个元素时并不是创建一个新地址，而是直接指向s的元素[0]，即id(s[:1])==id(s[0])

l = [1,2,3,4,5]
l1 = l[:]
print(l)
print(l1)
print(id(l))
print(id(l1))
print()         # list完整切片创建出一个新的list，因此地址不同。list部分切片也是如此

'''
123456789
123456789
1442735811184
1442735811184

123456
123456
1442735818096
1442735817816

1
1
1
1442705472792
1442705472792
1442705472792

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
1442735810760
1442734941768
'''

#1 S.capitalize() 将字符串首字母大写，其余小写，返回字符串
s = "i LOVE LWY"
print(s.capitalize())   # I love lwy

#2 S.title()      按照标题格式进行大小写转换（每个单词首字母大写），返回字符串
print(s.title())        # I Love Lwy

#3 S.upper()      将所有英文字符变为大写，返回字符串
s = "i love lwy"
print(s.upper())        # I LOVE LWY

#4 S.lower()      将所有英文字符变为小写，返回字符串
s = "I LOVE LWY"
print(s.lower())        # i love lwy

#5 S.swapcase()   大小写交互换，返回字符串
s = "I love lwy"
print(s.swapcase())     # i LOVE LWY
print()

#6 len(S)     计算字符串的字符个数,以后也可以用于计算元组列表等序列（个数≠长度）
s = "Study makes me happy"
s1 = "Study makes me 快乐happy"
print(len(s))   # 20
print(len(s1))  # 22

#7 S.count()  计算字符串中出现指定字符串的次数，返回整型
print(s.count("t",0,1))   # 0  [start, [end]]含左不含右
print()

#8 S.find()   查找字符串中是否具有指定的字符串，返回第一次出现的位置（下标），查找不到返回-1
#  S.rfind()  反向查找
print(s.find("a",3,9))    # 7 [start, [end]]含左不含右
print(s.find("z",0,1))    # -1

#9 S.index()  查找字符串中是否具有指定的字符串，返回第一次出现的位置（下标），查找不到直接报错
#  S.rindex() 反向查找
print(s.index("a",3,9))   # 7 [start, [end]]含左不含右
#print(s.index("z",0))  Error

#10 S.startswith()  检测字符串是否以指定的字符串开头(可指定起始检测位置)，返回布尔值
print(s.startswith("S"))    # True
print(s.startswith("t",1))  # True
print(s.startswith("t",0))  # False

#11 S.endswith()    检测字符串是否以指定的字符串结尾(可指定起始检测位置)，返回布尔值
print(s.endswith("y"))      # True
print(s.endswith("h"))      # False
print()

#12 S.is()    is开头的函数，返回值都是布尔值
s = "Study makes me happy"
print(s.istitle())  # 检测每个单词的首字母是否都是大写，返回布尔值
print(s.isupper())  # 检测所有英文字符是否都是大写，返回布尔值。若存在非英文字符，只管英文字符，若无英文字符均为假。即"我爱 PYTHON 1314！おはよう！"为真，"我爱"、"  "、""均为假
print(s.islower())  # 检测所有英文字符是否都是小写，返回布尔值。若存在非英文字符，只管英文字符，若无英文字符均为假。即"我爱 PYTHON 1314！おはよう！"为真，"我爱"、"  "、""均为假
print(s.isspace())  # 检测是否是空字符串，返回布尔值
print()
s = "我爱 PYTHON 1314！おはよう！"
s1 = "PYTHON"
s2 = "我爱おはようαβ"
s3 = "我爱おはようαβ1314"
s4 = "!!!!!"
s5 = "     "
s6 = ""
print(s.isalpha())  # 检测字符串是否由alpha语言组成（元组关系演算语言），返回布尔值
print(s1.isalpha()) # True
print(s2.isalpha()) # True
print(s3.isalpha()) # False
print(s4.isalpha()) # False
print(s5.isalpha()) # False
print(s6.isalpha()) # False
print()
s = "52you"
s1 = "52"
s2 = "you"
print(s.isalnum())  # 检测字符串是否由alpha语言和（或）数字组成，返回布尔值
print(s1.isalnum()) # True
print(s2.isalnum()) # True
print()
s = "1314５２０"
print(s.isdigit())  # 检测字符串是否由阿拉伯数字字符(0123456789)组成
print(s.isdecimal())# 检测字符串是否由十进制字符组成
print(s.isnumeric())# 检测字符串是否由数字字符（1一壹Ⅰ）组成
'''
isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节）
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''

#13 S.split()         使用指定的字符将字符串卷分离成多个字符串，返回列表
#   S.split()         反向切割，同样是按S中的字符顺序返回list，并非是反向返回的
s = "日照香炉生紫烟*遥看瀑布挂前川*飞流直下三千尺*疑是银河落九天"
print(s.split("*",1))   # ['日照香炉生紫烟', '遥看瀑布挂前川*飞流直下三千尺*疑是银河落九天']
print(s.rsplit("*",1))  # ['日照香炉生紫烟*遥看瀑布挂前川*飞流直下三千尺', '疑是银河落九天']

#14 S.partition()     同样是切割，split可指定次数切割多次，partition只能切割一次且返回值包含切割符，返回元组
print(s.partition("*"))
print(type(s.partition("*")))
'''
在S中搜索分隔符，并返回它之前的部分，分隔符本身，以及后面的部分。如果没有找到分隔符，则返回S和两个空字符串。
'''


#14 S.splitlines()    使用\n，\r或者\r\n将字符串卷分离成多个字符串，返回列表
s= "日照香炉生紫烟\n遥看瀑布挂前川\r飞流直下三千尺\r\n疑是银河落九天。"
print(s.splitlines())   # ['日照香炉生紫烟', '遥看瀑布挂前川', '飞流直下三千尺', '疑是银河落九天。']
print(s.splitlines(-5)) # ['日照香炉生紫烟\n', '遥看瀑布挂前川\r', '飞流直下三千尺\r\n', '疑是银河落九天。']
'''
特别说明
S.splitlines() 如果不设参数，以'\n'、'\r'、'\r\n'进行分割，在行边界处断开，'\n'、'\r'、'\r\n'不包括在列表内，如果设了参数且参数为True，则将'\n'、'\r'、'\r\n'n也一并返回
'''

#15 S.join(iterable)  使用指定的字符串作为连接符将序列中的内容连接成新的字符串，返回字符串
s1 = "*"
print(s1.join(s))

'''
这三种写法都是可以的：
s = "日照香炉生紫烟，遥看瀑布挂前川。""飞流直下三千尺，疑是银河落九天。"

s = "日照香炉生紫烟，遥看瀑布挂前川。"\
    "飞流直下三千尺，疑是银河落九天。"
    
s = "日照香炉生紫烟，遥看瀑布挂前川。\
飞流直下三千尺，疑是银河落九天。"

有一个字符串很长，如何写成多行？
方法一
使用续行符：
sql = "select * "\
" from a "\
" where b = 1"

但是高版本python可能会不支持此方式，且每次都要在行最后加上续行符，不够简洁。

方法二
使用括号：
sql = ("select *"
" from a "
" where b = 1")
'''

#16 S.ljust()     将字符串靠左对齐，可指定字符串长度，可在空白处填充指定字符（默认填充空格），返回字符串
s = "对齐"
print(s.ljust(5,"l"))   # 对齐lll

#17 S.center()    将字符串居中对齐，可指定字符串长度，可在空白处填充指定字符（默认填充空格），返回字符串
print(s.center(5,"c"))  # cc对齐c

#18 S.rjust()     将字符串靠右对齐，可指定字符串长度，可在空白处填充指定字符（默认填充空格），返回字符串
print(s.rjust(5,"r"))   # rrr对齐

#19 S.lstrip()    去除字符串左侧的指定字符串（直到新字符串最左侧不含指定字符串），默认去除空格，返回字符串
s = " abc去除"
print(s.lstrip("a"))# 从字符串开头第一个字符开始算，若指定字符串不是在字符串的起点，则不会去除任何字符
print(s.lstrip(" a"))   #  abc去除

#19 S.rstrip()    去除字符串右侧的指定字符串（直到新字符串最右侧不含指定字符串），默认去除空格，返回字符串
s = "去除abc "
print(s.rstrip("c"))# 从字符串结尾第一个字符开始算，若指定字符串不是在字符串的终点，则不会去除任何字符
print(s.rstrip("c "))   # 去除ab

#20 S.strip()     去除字符串两侧的指定字符串（直到新字符串两侧不含指定字符串），默认去除空格，返回字符串
s = "abcd去除fgi"
print(s.strip("abdfi")) # cd去除fg
print(s.strip("ifabd")) # cd去除fg
'''
此处注意：
strip()和lstrip()及rstrip()不同的是：

strip()是将指定字符串拆分成字符来执行，只要S两侧任何一侧（最左 和/或 最右）含有指定字符串中的任意一个字符，那么就会被去除，
也就是说，strip()的执行是不断循环检测S两侧是否存在指定字符串中的任意一个字符并去除，只有当两侧都不再存在相应字符，strip()才会终止，返回新字符串
S = "abcdefg"     S.strip("abdfg")的返回值是"cde"
'''

#21 S.zfill() # 将字符串靠右对齐，可指定字符串长度，在空白处填充0，返回字符串
s = "零填充"
print(s.zfill(9))   # 000000零填充

#22 S.replace(被替换字符串,替换字符串)   # 字符串替换操作，用于长字符替换
s = "我要睡。觉了。。 "
s1 = "。要。要。要 "

print(s.replace("。","！",1)) # 我要睡觉了！。
print(s.replace("。。","！！"))# 我要睡觉了！！

#23 S.maketrans('被替换的字符串','生成一个用于字符串替换的映射表，为了给translate函数使用，返回映射表
#24 S.translate(S.maketrans) 进行字符串翻译操作，类似转换，用于多字符替换
a = s2.maketrans("要。","my") # s2可以是空值，且只是形式，可不定义s2。等于只是给不同的maketrans命名用于区分
print(a)                # {12290: 109, 35201: 121}
print(s.translate(a))   # 我m睡y觉了yy  即 要——m  。——y

'''
maketrans(x, y=None, z=None, /):
如果只有一个参数，它必须是一个字典，映射Unicode顺序（整数）或字符到Unicode序数、字符串或None。字符键将被转换为序数。
如果有两个参数，它们必须是相等长度的字符串，在结果字典中，x中的每个字符都将被映射到y中的相同位置的字符。
如果有第三个参数，它必须是一个字符串，其字符将被映射到结果中的None。
'''

# 补充资料：https://blog.csdn.net/jacky_zhuyuanlu/article/details/79789801



'''
"E:\Python workspace\PycharmProjects\习题课\venv\Scripts\python.exe" "E:/Python workspace/PycharmProjects/习题课/07-S.py"
<class 'S'>
123456789
123456789
2418761296432
2418761296432

123456
123456
2418761304920
2418761304976

1
1
1
2418759335192
2418759335192
2418759335192

[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
2418761296072
2418760427080

I love lwy
I Love Lwy
I LOVE LWY
i love lwy
i LOVE LWY

20
22
0

7
-1
7
True
True
False
True
False

False
False
False
False

False
True
True
False
False
False
False

True
True
True

True
True
True
['日照香炉生紫烟', '遥看瀑布挂前川*飞流直下三千尺*疑是银河落九天']
['日照香炉生紫烟*遥看瀑布挂前川*飞流直下三千尺', '疑是银河落九天']
('日照香炉生紫烟', '*', '遥看瀑布挂前川*飞流直下三千尺*疑是银河落九天')
<class 'tuple'>
['日照香炉生紫烟', '遥看瀑布挂前川', '飞流直下三千尺', '疑是银河落九天。']
['日照香炉生紫烟\n', '遥看瀑布挂前川\r', '飞流直下三千尺\r\n', '疑是银河落九天。']
日*照*香*炉*生*紫*烟*
*
*疑*是*银*河*落*九*天*。
对齐lll
cc对齐c
rrr对齐
 abc去除
bc去除
去除abc 
去除ab
cd去除fg
cd去除fg
000000零填充
我要睡！觉了。。 
我要睡。觉了！！ 
{35201: 109, 12290: 121}
我m睡y觉了yy 

Process finished with exit code 0
'''