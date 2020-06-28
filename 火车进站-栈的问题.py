"""题目描述
给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，
火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求以字典序排序输出火车出站的序列号。
输入描述:
有多组测试用例，每一组第一行输入一个正整数N（0<N<10），第二行包括N个正整数，范围为1到9。
输出描述:
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。"""


def find(a, b, c):
    if not a and not b:
        res.append(' '.join(map(str, c)))
    if b:
        c.append(b.pop())
        find(a, b, c)
        b.append(c.pop())
    if a:
        b.append(a.pop(0))
        find(a, b, c)
        a.insert(0, b.pop())


while True:
    try:
        res = []
        n = int(input())
        pre = list(map(int, input().split()))
        ins, outs = [], []
        find(pre, ins, outs)
        res.sort()
        for i in res:
            print(i)
    except:
        break
