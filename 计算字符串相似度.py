"""对于不同的字符串，我们希望能有办法判断相似程度，我们定义了一套操作方法来把两个
不相同的字符串变得相同，具体的操作方法如下：
1 修改一个字符，如把“a”替换为“b”。
2 增加一个字符，如把“abdd”变为“aebdd”。
3 删除一个字符，如把“travelling”变为“traveling”。
比如，对于“abcdefg”和“abcdef”两个字符串来说，我们认为可以通过增加和减少一个“g”的方式来达到目的。
上面的两种方案，都只需要一次操作。把这个操作所需要的次数定义为两个字符串的距离，而相似度等于“距离＋1”的倒数。
也就是说，“abcdefg”和“abcdef”的距离为1，相似度为1/2=0.5.
给定任意两个字符串，你是否能写出一个算法来计算出它们的相似度呢？
请实现如下接口

 /* 功能：计算字符串的相似度
  * 输入：pucAExpression/ pucBExpression：字符串格式，如: "abcdef"
  * 返回：字符串的相似度,相似度等于“距离＋1”的倒数,结果请用1/字符串的形式,如1/2
  */
 public static  String  calculateStringDistance(String expressionA, String expressionB)
 {
     /* 请实现*/
     return null;
 }
约束：
1、PucAExpression/ PucBExpression字符串中的有效字符包括26个小写字母。
2、PucAExpression/ PucBExpression算术表达式的有效性由调用者保证;
3、超过result范围导致信息无法正确表达的，返回null。
输入描述:
输入两个字符串

输出描述:
输出相似度，string类型"""


def editDistance(str1, str2):
    len1, len2 = len(str1) + 1, len(str2) + 1
    dp = [[0 for i in range(len2)] for j in range(len1)]
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j
    for i in range(1, len1):
        for j in range(1, len2):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return dp[-1][-1]


while True:
    try:
        print("1/" + str(editDistance(input(), input()) + 1))
    except:
        break