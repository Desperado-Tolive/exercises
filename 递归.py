# 类似与栈的先进后出模式
def digui(num):
    print(num)
    if num > 0:
        digui(num - 1)
    else:
        print("=" * 10)
    print(num)
digui(5)