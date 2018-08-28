以字符串为例，谈谈Python到底要学到什么程度
2018年04月02日 15:15:41 阅读数：115更多
个人分类： python
所属专栏： Python基础教程
版权声明：本文为博主原创文章，未经博主允许不得转载。 https://blog.csdn.net/jacky_zhuyuanlu/article/details/79789801

    古语云：慈不掌兵，义不为商；离商业越近，离人性越远；我们在自学数据科学时，一定会辅助一些书籍或者视频来学习，怎么学习，选择哪些资料来学习?这时，我们都要理解好第一句话，理解不好，浪费钱是次要，重要的是还会浪费我们的时间；

    对于学习数据科学这门技术来说，一切速成，都只是拔苗助长；数据分析不能速成，数据挖掘不能速成，7天，1个月，都不可能学到什么，钻研一门技术6个月，你也只能会有一点入门的感觉，而已；听上去有点荒凉是吧，可忠言逆耳；

    Python仅仅是一门编程语言，以后小学都普及了，现在却被培训机构捧上了天，欲让其灭亡，必先让其膨胀，对于Python来说，这并不是什么好事，对于学习Python的人来说，这更不是什么好事，学习技术跟学武一样，要内外兼修，内功扎实才能厚积薄发；可这个浮躁的社会，要做到这点耐得住寂寞的修炼内功，不容易；人性的弱点是：急于想要得到好处与回报；

    那么问题抛出来了，我们该如何学习一门技能呢，我拿Python学习举例，说说我的看法；

    学习没有捷径，但一定有方法，有很多朋友问我：Python到底怎么学，要学到什么程度，在工作中才够用？今天，jacky以字符串的学习为例，谈谈Python我们到底要学到什么程度，要怎么学？

（一）入门水平
1.1入门水平我们能做什么？

    很遗憾的说，对于零基础的朋友来说，入门水平，只能提高我们学习Python的兴趣，仅此而已；
        零基础学Python的朋友，由于缺少专业背景和实操背景，仅靠短时间的自学，大部分都也只是入门水平，大家还要继续学习，不要学到这里就停下了，坚持学习，才能看到阳光；

1.2 掌握哪些知识点才算入门

    1) 知道字符串是干什么的？
        用于在程序中显示消息的（比如游戏里的”准备”和”游戏结束”这样的消息）

    2)知道如何创建字符串

        英文半角引号
            知道单引号，双引号，三引号的区别；

    3)知道如何在字符串里嵌入值
        占位符%s

>>>myscore = 100
>>>message='I scored %s points'
>>>print(message % myscore)
I scored 100 points


    4)知道字符串乘法

>>>print(10*'a')
aaaaaaaaaa

    1
    2

（二）初级水平
2.1 初级水平我们能做什么？

    做一些数据分析类的辅助工作，足够了，但是对于数据工程师或挖掘师来说，差的还太远；
        我们有时会自我膨胀，对于外行人可能还会炫耀一下，但是对于有经验的老手来说，初级水平离实操还有很长的一段差距

2.2 掌握哪些知识点才算初级水平

    掌握如下字符串功能（具体讲解见中级水平部分）

        移除空白

        分割

        长度

        索引

        切片

（三）中级水平
3.1 中级水平我们能做什么？

    中级水平，我们只能跟别人说，Python我学过；学到中级水平我们才有可能知道，原理工作中，我们要学的东西太多了，学习中的所有技巧，对于工作来说，都是最重要的技巧；积累很重要，学无止境；

3.2 中级水平我们需掌握－查看字符串的所有功能

temp = 'jacky'
help(type(temp))


功能1：capitalize(首字母大写)

def capitalize(self):  # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str

        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return
    # 首字母大写
    # >>> a = "abel"
    # >>> b = a.capitalize()
    # >>> b
    # 'Abel'


功能2：center(内容居中空白填充)

    def center(self, width, fillchar=None):  # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str

        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""
    # 内容居中,width: 总长度; fillchar:空白处填充内容,默认无
    # >>> a
    # 'Abel'
    # >>> b = a.center(20, '#')
    # >>> b
    # '########Abel########'


功能3：count(子序列个数)

    def count(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int

        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0
    # 子序列个数
    # >>> a = "Abelisgood"
    # >>> b = a.count('o')
    # >>> b
    # 2
    # >>> b = a.count('o', 0, 8)
    # >>> b
    # 1


功能4：endswith(判断是否以**结束)

def endswith(self, suffix, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool

        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False
    # 判断str是否以xxx 结束
    # >>> a
    # 'Abelisgood'
    # >>> b = a.endswith('d')
    # >>> b
    # True
    # >>> b = a.endswith('g', 0, 7)
    # >>> b
    # True


功能5：expandtabs (讲tab转换成空格)

 def expandtabs(self, tabsize=8):  # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str

        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""
    # 将tab转换成空格,默认一个tab转换成8个空格
    # >>> a = "a\tbel"
    # >>> b= a.expandtabs()
    # >>> b
    # 'a       bel'(8个空格)


功能6：find(寻找子序列位置)

 def find(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int

        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0
    # 寻找子序列位置,如果没有找到,返回-1
    # index没有找到,直接报错
    # >>> a = "asdfjsdakfwejfi"
    # >>> b = a.find('f', 0, 11)
    # >>> b
    # 3
    # >>> b = a.find('z')
    # >>> b
    # -1


功能7：format(字符串格式化)

def format(self, *args, **kwargs):  # known special case of str.format
        """
        S.format(*args, **kwargs) -> str

        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        pass
    # 字符串格式化,动态参数。可以拼接字符串。
    # >>> a = "abel {0} good {1}"
    # >>> b = a.format('is', 'man')
    # >>> b
    # 'abel is good man'
    # >>> 
    def format_map(self, mapping):  # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str

        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""


功能8：index(返回索引位置)

def index(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int

        Like S.find() but raise ValueError when the substring is not found.
        """
        return 0
    # 返回索引位置;可先参数，start:起始位置，end:结束位置，返回一个整数类型(当字符串没有找到时，会提示报错信息)
    # >>> a = "asdfjsdakfwejfi"
    # >>> b = a.index('z')
    # Traceback (most recent call last):
    # File "<pyshell#22>", line 1, in <module>
    #     b = a.index('z')
    # ValueError: substring not found


功能9：isalnum(字符数字组合判断)

def isalnum(self):  # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool

        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False
    # 字符串都是字符，数字 或是字符数字组合则为True否则为False
    # >>> a
    # 'asdfjsdakfwejfi'
    # >>> b = a.isalnum()
    # >>> b
    # True

    # >>> a = ' '
    # >>> b = a.isalnum()
    # >>> b
    # False


功能10：isalpha(字母判定)

def isalpha(self):  # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool

        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False
    # 字符串中有一个为字母或所有都是字母都 True 否则为False
    # >>> a
    # 'abel20'
    # >>> b = a.isalpha()
    # >>> b
    # False


功能11：isdecimal(十进制判定)

 def isdecimal(self):  # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool

        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False
    # 如果只有十进制则返回True，否则返回False
    # >>> a = 'abel20'
    # >>> b = a.isdecimal()
    # >>> b
    # False


功能12：isdecimal(全部为数字判定)

def isdigit(self):  # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool

        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False
    # 元素全部为数字时返回 True否则返回 False
    # >>> a
    # 'abel20'
    # >>> b = a.isdigit()
    # >>> b
    # False   


功能13：isidentifier(合法标识符判定)

def isidentifier(self):  # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool

        Return True if S is a valid identifier according
        to the language definition.

        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False
    # 判断字符串是否是合法的标识符(标识符必须合法)返回bool类型
    # >>> a = '5'
    # >>> b = a.isidentifier()
    # >>> b
    # False
    # >>> a = 'abel342'
    # >>> b = a.isidentifier()
    # >>> b
    # True


功能14：islower(小写判定)

    def islower(self):  # real signature unknown; restored from __doc__
        """
        S.islower() -> bool

        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False
    # 判断字符串中字母是否都是小写，返回bool类型
    # >>> a
    # 'abel342'
    # >>> b = a.islower()
    # >>> b
    # True

    # >>> a = 'Abel83'
    # >>> b = a.islower()
    # >>> b
    # False


功能15：isnumeric(判断字符串中是否都是数字)

def isnumeric(self):  # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool

        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False
    # 判断字符串中是否都是数字，返回bool类型
    # >>> a = 'abel349'
    # >>> b = a.isnumeric()
    # >>> b
    # False
    # >>> a = '123'
    # >>> b = a.isnumeric()
    # >>> b
    # True


功能16：isprintable(判断是不是只包含可打印字符)

    def isprintable(self):  # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool

        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False
    # 判断是不是只包含可打印字符，返回Bool值
    # >>> a
    # '天天向上\t2016'
    # >>> b = a.isprintable()
    # >>> b
    # False
    # >>> q = 'this is test'
    # >>> b = a.isprintable()
    # >>> b
    # False


功能17：isspace(判断是不是只包含空格字符)

 def isspace(self):  # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool

        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False
    # 判断是不是只包含空格字符，返回bool值



功能18：istitle(判断是不是只包含空格字符)

    def istitle(self):  # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool

        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False
    # 判断是不是每个词的首字母是不是大写，返回Bool值。一般标题会使用


功能19：isupper(判断字符串是不是都是大写)

def isupper(self):  # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool

        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False
    # 判断字符串是不是都是大写，返回bool值



功能20：join(返回通过指定字符分隔的新字符串)

 def join(self, iterable):  # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str

        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""
    # 返回通过指定字符分隔的新字符串
    # >>> a = ['a', 'b', 'c', 'f']
    # >>> b = "_".join(a)
    # >>> b
    # 'a_b_c_f'



功能21：ljust(左对齐，右添充)

    def ljust(self, width, fillchar=None):  # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str

        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""
    # 左对齐，右添充，参数width 宽度(fillchar 添充字符，默认是空格)



功能22：lower(转换为小写)

def lower(self):  # real signature unknown; restored from __doc__
        """
        S.lower() -> str

        Return a copy of the string S converted to lowercase.
        """
        return ""
    # 转换为小写



功能23：lstrip(删除左边的空白或自定义的字符)

def lstrip(self, chars=None):  # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str

        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""
    # 删除左边的空白或自定义的字符
    # >>> a = "   Hi, I'm Abel"
    # >>> b = a.lstrip()
    # >>> b
    # "Hi, I'm Abel"



功能24：maketrans(替换相应的字符)

def maketrans(self, *args, **kwargs):  # real signature unknown
        """
        Return a translation table usable for str.translate().

        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass
    # str.translate()函数配合使用，替换相应的字符

功能25：partition(拆分字符串)

def partition(self, sep):  # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)

        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass
    # 用于拆分字符串，返回一个包含三个元素的元组;返回一个包含三个元素的元组。如果指定的字符串sep不存在，则返回自己加两个空元素。
    # >>> a = "Hi, I'm abel"
    # >>> b = a.partition('a')
    # >>> b
    # ("Hi, I'm ", 'a', 'bel')
    # >>> c = a.partition('z')
    # >>> c
    # ("Hi, I'm abel", '', '')



功能26：replace(替换)

def replace(self, old, new, count=None):  # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str

        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""
    # 使用新的字符串替换老的字符串(可选参数count 指定替换的次数，默认是全部)
    # >>> a = "Abelisgood"
    # >>> b = a.replace('o', 'z')
    # >>> b
    # 'Abelisgzzd'
    # >>> b = a.replace('o', 'z', 1)
    # >>> b
    # 'Abelisgzod'



功能27：rfind(反向查找)

def rfind(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int

        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.

        Return -1 on failure.
        """
        return 0
    # 反向查找，与find 是相反方向 



功能28：rindex(反向索引)

    def rindex(self, sub, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int

        Like S.rfind() but raise ValueError when the substring is not found.
        """
        return 0
    # 返回字符串所在的索引，与index 相反方向



功能29：rjust(右对齐，右填充)

def rjust(self, width, fillchar=None):  # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str

        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""
    # 右对齐，右填充。与ljust 相反



功能30：rpartition(反向拆分)

def rpartition(self, sep):  # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)

        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass
    # 拆分：与 partition相反，只不过是从字符串的右边开始拆分。



功能31：rsplit(右边拆分)

def rsplit(self, sep=None, maxsplit=-1):  # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings

        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []
    # 与split类似，从右边开始拆分，返回一个列表类型,（可选参数maxsplit 每次+- 1  sep 的值默认是空格）

功能32：split(左边拆分)

def split(self, sep=None, maxsplit=-1):  # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings

        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []
    # 从左边开始拆分，返回一个列表类型,（可选参数maxsplit 每次+- 1  sep 的值默认是空格）


功能33：split(生成新列表)

    def splitlines(self, keepends=None):  # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings

        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []
    # 拆分多行字符串，以每行一个元素生成一个新的列表，如果是单行字符串，则返回原字符串


功能34：startswith(是否以字符串开始)

def startswith(self, prefix, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool

        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False
    # 是否以字符串开始(可选参数，start与end 分别代表起始和结束),返回bool值


功能35：strip(去除左边空白或自定义字符串)

def strip(self, chars=None):  # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str

        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""
    # 去除左边空白或自定义字符串


功能36：swapcase(把字符串的大小写字母互换输出)

 def swapcase(self):  # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str

        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""
    # 把字符串的大小写字母互换输出

 

功能37：title(字符串首字母大写，其他全部小写)

 def title(self):  # real signature unknown; restored from __doc__
        """
        S.title() -> str

        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""
    # 字符串首字母大写，其他全部小写

功能38：translate(str.maketrans()函数配合使用，替换相应的字符)

def translate(self, table):  # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str

        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""
    # str.maketrans()函数配合使用，替换相应的字符

功能39：upper(全部转换为大写)

def upper(self):  # real signature unknown; restored from __doc__
        """
        S.upper() -> str

        Return a copy of S converted to uppercase.
        """
        return ""
    # 与lower 相反，全部转换为大写

功能40：zfill(回一个添充的字符串)

def zfill(self, width):  # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str

        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""
    # 回一个添充的字符串，width 添写长度，如果长宽和字符串相等，则直接返回字符串本身，如果长度大于字符串，则用0添充至指定的长度