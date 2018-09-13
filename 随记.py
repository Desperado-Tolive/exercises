# 关于if
s = "12"
if s.isalnum()==1:  # 结合分析，也就是说在if中 "==" 本质是判断符，（即 a==1 是 "a是否是1" 而非 "a是否等于1"，也就是说判断a与1的地址是不是相同的）此猜想验证为错误，"==" 本质是判断值是否相同
    print(1)
else:
    print(2)


s = "12"
if s.isalnum():     # 由上下对比可分析出，if的本质是接受布尔值，若接收到的布尔值是True则执行语句块，False则不执行
    print(1)
else:
    print(2)

if True:            # 也就是说甚至可以这样写
    print(1)
else:
    print(2)


print(id(257))
a = 257
b = 257
print(a==b)