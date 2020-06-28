"""题目描述
连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
首先输入一个整数，为要输入的字符串个数。
例如：
输入：2
abc
12345789
输出：abc00000
12345678
90000000"""


while True:
    try:
        a= int(input())
        for i in range(a):
            s=input()
            while len(s)>8:
                print(s[:8])
                s=s[8:]
            print(s.ljust(8,"0"))
    except:
        break