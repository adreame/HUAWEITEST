"""题目描述
将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变
输入
Jkdi234klowe90a3
输出
Jkdi*234*klowe*90*a*3*"""

import re

while True:
    try:
        print(re.sub(r'(\d+)', '*\g<1>*', input()))
    except:
        break
