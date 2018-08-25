# 1 三角
for i in range(5):
    for j in range(i + 1):
        print("* ", end="")
    print()
'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

print()

# 2 空三角
for i in range(5):
    for j in range(i + 1):
        # if i == 0 or i == 1 or i == 4:
        if i == 4:
            print("* ", end="")
        else:
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()
'''
for i in range (5):
    for j in range(i+1):
        if i == 4 or j == 0 or j == i:
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()

* 
* * 
*   * 
*     * 
* * * * * 
'''

print()

# 3 倒三角
for i in range(5, 0, -1):  # i仅需控制行数即可
    for j in range(i):  # i与大小列数的关系不是绝对的，列数只要是递减就可以，这可以通过其它变量或关系式控制（如5-i）
        print("* ", end="")  # 从以上两条得出，用变量控制for循环，我们所需要的是循环次数，而非变量本身的大小
    print()  # 如果需要i参与到for循环内对某变量的控制（或直接是i本身），则i本身的大小也是重要的，需要着重考虑
    # 先考虑能否直接用i，再考虑能否用含i的关系式，如果都不能解决则放弃用i，使用其它变量来控制
'''
for i in range(5):              # i仅需控制行数即可
    for j in range(5-i):        # i的大小与列数的关系不是绝对的，列数只要是递减就可以，这可以通过其它变量或关系式控制（如5-i）
        print("* ",end = "")    # 从以上两条得出，用变量控制for循环，我们所需要的是循环次数，而非变量本身的大小
    print()                     # 如果需要i参与到for循环内对某变量的控制（或直接是i本身），则i本身的大小也是重要的，需要着重考虑。
                                # 先考虑能否直接用i，再考虑能否用含i的关系式，如果都不能解决则放弃用i，使用其它变量来控制

* * * * * 
* * * * 
* * * 
* * 
* 
'''

print()

# 4 空倒三角
for i in range(5, 0, -1):
    for j in range(i):
        # if i == 1 or i == 2 or i == 5:
        if i == 5:
            print("* ", end="")
        else:
            if j == 0 or j == i - 1:
                print("* ", end="")
            else:
                print("  ", end="")
    print()

'''
for i in range(5):
    for j in range(5-i):
        if i == 0:
            print("* ",end = "")
        else:
            if j == 0 or j == 5-i-1:
                print("* ",end = "")
            else:
                print("  ",end = "")
    print()

* * * * * 
*     * 
*   * 
* * 
* 
'''

print()

# 5 反三角
for i in range(5):
    for m in range(4 - i):
        print("  ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

print()

# 6 空反三角
for i in range(5):
    for m in range(4 - i):
        print("  ", end="")
    for j in range(i + 1):
        if i == 4:
            print("* ", end="")
        else:
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()
'''
        * 
      * * 
    *   * 
  *     * 
* * * * * 
'''

print()

# 7 正三角
for i in range(5):
    for m in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

print()

# 8 空正三角
for i in range(5):
    for m in range(4 - i):
        print(" ", end="")
    for j in range(i + 1):
        if i == 4:
            print("* ", end="")
        else:
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
    print()
'''
    * 
   * * 
  *   * 
 *     * 
* * * * * 
'''