"""题目描述
功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
返回:转换成功返回 0 ,非法输入与异常返回-1
本题为多组输入，请使用while(cin>>)等形式读取数据
输入描述:
输入一个正整数。
输出描述:
输出一个相加后的整数。"""


while True:
    try:
        n = int(input())
        s, b = 0, -1
        for i in range(n):
            b += 3
            s += b
        print(s)
    except:
        break