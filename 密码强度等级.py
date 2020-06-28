"""题目描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符
二、字母:
0 分: 没有字母
10 分: 全都是小（大）写字母
20 分: 大小写混合字母
三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字
四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号
五、奖励:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号
最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱
对应输出为：
VERY_SECURE
SECURE,
VERY_STRONG,
STRONG,
AVERAGE,
WEAK,
VERY_WEAK,
请根据输入的密码字符串，进行安全评定。
注：
字母：a-z, A-Z
数字：-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
!"#$%&'()*+,-./     (ASCII码：x21~0x2F)
:;<=>?@             (ASCII<=><=><=><=><=>码：x3A~0x40)
[\]^_`             (ASCII码：x5B~0x60)
{|}~                (ASCII码：x7B~0x7E)
接口描述：
Input Param
String pPasswordStr:    密码，以字符串方式存放。
Return Value
根据规则评定的安全等级。
public static Safelevel GetPwdSecurityLevel(String pPasswordStr)
{
/*在这里实现功能*/
return null;
}
输入描述:
输入一个string的密码

输出描述:
输出密码等级"""


def GetScore(s):
    score, d, c_h, c_l, c = 0, 0, 0, 0, 0
    for i in s:
        if 48 <= ord(i) <= 57:
            d += 1
        elif 97 <= ord(i) <= 122:
            c_l += 1
        elif 65 <= ord(i) <= 90:
            c_h += 1
        elif 0x21 <= ord(i) <= 0x2f or 0x3a <= ord(i) <= 0x40 or 0x5b <= ord(i) <= 0x60 or 0x7b <= ord(i) <= 0x7e:
            c += 1
    # 一、密码长度
    if len(s) <= 4:
        score += 5
    elif 4 < len(s) < 8:
        score += 10
    else:
        score += 25
    # 二、字母
    if c_h and c_l == 0 or c_h == 0 and c_l:
        score += 10
    elif c_h and c_l:
        score += 20
    # 三、数字
    if d == 1:
        score += 10
    elif d > 1:
        score += 20
    # 四、符号
    if c == 1:
        score += 10
    elif c > 1:
        score += 25
    # 五、奖励
    if c_h + c_l and d and not c:
        score += 2
    elif (c_h and c_l == 0 or c_h == 0) and c_l and d and c:
        score += 3
    elif c_h and c_l and d and c:
        score += 5
    if score >= 90:
        print('VERY_SECURE')
    elif 80 <= score < 90:
        print('SECURE')
    elif 70 <= score < 80:
        print('VERY_STRONG')
    elif 60 <= score < 70:
        print('STRONG')
    elif 50 <= score < 60:
        print('AVERAGE')
    elif 25 <= score < 50:
        print('WEAK')
    else:
        print('VERY_WEAK')


while True:
    try:
        s = input()
        GetScore(s)
    except:
        break
