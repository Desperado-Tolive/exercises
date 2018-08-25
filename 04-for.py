#1 长方形
for i in range(0,4):
    for j in range(0,5):
        print("* ",end = "")
    print()

'''
a = 5
for i in range(0,4):
    print("* " * a)

* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

print()

#2 空长方形
for i in range(4):
    for j in range(5):
        if i == 0 or i == 3:
            print("* ",end = "")
        else:
            if j == 0 or j == 4:
                print("* ",end = "")
            else:
                print("  ",end = "")
    print()
'''
for i in range(4):
    for j in range(5):
        if i == 0 or i == 3 or j == 0 or j == 4:
            print("* ",end = "")
        else:
            print("  ",end = "")
    print()

* * * * * 
*       * 
*       * 
* * * * * 

错误示范
for i in range(4):
    if i == 0 or i == 3:
        for j in range(5):
            print("* ",end = "")
    else:
        for j in range(5):
            if j == 0 or j ==4:
                print("* ",end = "")
            else:
                print("  ",end = "")
    print()
'''