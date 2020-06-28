"""题目描述
题目标题：
判断短字符串中的所有字符是否在长字符串中全部出现
详细描述：
接口说明
原型：
boolIsAllCharExist(char* pShortString,char* pLongString);

输入参数：
  char* pShortString：短字符串
    char* pLongString：长字符串
输入描述:
输入两个字符串。第一个为短字符，第二个为长字符。

输出描述:
返回值："""


while True:
    try:
        s, l = input(), input()
        for i in range(len(s)):
            if s[i] not in l:
                print('false')
                break
            if i == len(s)-1:
                print('true')
    except:
        break