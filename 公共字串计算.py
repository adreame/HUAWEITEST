"""题目描述
题目标题：
计算两个字符串的最大公共字串的长度，字符不区分大小写
详细描述：
接口说明
原型：
int getCommonStrLength(char * pFirstStr, char * pSecondStr);
输入参数：
     char * pFirstStr //第一个字符串
     char * pSecondStr//第二个字符串
输入描述:
输入两个字符串

输出描述:
输出一个整数"""


while True:
    try:
        s1, s2, n = input(), input(), []
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        for i in range(len(s1)-1):
            for j in range(i+1,len(s1)):
                if s1[i:j] in s2:
                    n.append(j-i)
        n.sort(reverse=True)
        print(n[0])
    except:
        break