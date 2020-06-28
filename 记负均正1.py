"""题目描述
首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值，结果保留一位小数。

输入描述:
首先输入一个正整数n，
然后输入n个整数。

输出描述:
输出负数的个数，和所有正整数的平均值。"""


while True:
    try:
        N = int(input())
        nums = list(map(int, input().split()))
        n, m, t = 0, 0, 0
        for i in nums:
            if i < 0:
                n += 1
            elif i == 0:
                t += 1
            else:
                m += i
        print(n, round(m/(len(nums)-n-t),1))
    except:
        break