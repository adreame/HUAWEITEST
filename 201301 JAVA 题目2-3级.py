"""题目描述
编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，并且，
所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；
不满足时返回false。
输入描述:
第一行是数据个数，第二行是输入的数据

输出描述:
返回true或者false"""


def dfs(i, n, a, res, s):
    if i == n:
        return abs(res) == s
    else:
        return dfs(i + 1, n, a, res + a[i], s) or dfs(i + 1, n, a, res - a[i], s)


while True:
    try:
        n = int(input())
        l = list(map(int, input().split()))
        s1, s2 = 0, 0
        num = []
        for i in range(n):
            if l[i] % 5 == 0:
                s1 += l[i]
            elif l[i] % 3 == 0:
                s2 += l[i]
            else:
                num.append(l[i])
        d = abs(s1 - s2)
        if dfs(0, len(num), num, 0, d):
            print('true')
        else:
            print('false')
    except:
        break
