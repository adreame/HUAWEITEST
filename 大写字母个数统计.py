"""题目描述
找出给定字符串中大写字符(即'A'-'Z')的个数
接口说明
原型：int CalcCapital(String str);
返回值：int
输入描述:
输入一个String数据
输出描述:
输出string中大写字母的个数"""


while True:
    try:
        s, count = input(), 0
        for i in s:
            if i.isupper():
                count += 1
        print(count)
    except:
        break