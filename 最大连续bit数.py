"""题目描述
功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1

输入: 一个byte型的数字

输出: 无

返回: 对应的二进制数字中1的最大连续数
输入描述:
输入一个byte数字

输出描述:
输出转成二进制之后连续1的个数"""


import re

while True:
    try:
        s = int(input())
        num = bin(s)
        lis = re.findall(r'(1+)', str(num))
        lis = list(sorted(lis, key=lambda d: len(d), reverse=True))
        print(len(lis[0]))
    except:
        break