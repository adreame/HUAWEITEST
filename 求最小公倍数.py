"""题目描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

输入描述:
输入两个正整数A和B。

输出描述:
输出A和B的最小公倍数。

示例1
输入
5 7
输出  35"""

while True:
    try:
        m = input()
        a = int(m.split()[0])
        b = int(m.split()[1])
        if a > b:
            a, b = b, a
        for i in range(1, a*b):
            if b * i % a == 0:
                print(b*i)
                break
    except:
        break