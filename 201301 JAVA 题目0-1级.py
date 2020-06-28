"""题目描述
请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
输入描述:
输入两个正整数

输出描述:
返回结果"""


def dfs(m, n):
    if m == 0 or n == 0:
        return 1
    else:
        return dfs(m - 1, n) + dfs(m, n - 1)


while True:
    try:
        s = input().split()
        m, n = int(s[0]), int(s[1])
        print(dfs(m, n))
    except:
        break
