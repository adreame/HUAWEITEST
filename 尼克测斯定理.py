"""题目描述
验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
接口说明
原型：
 /*
 功能: 验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
 原型：
     int GetSequeOddNum(int m,char * pcSequeOddNum);
 输入参数：
     int m：整数(取值范围：1～100)
 返回值：
     m个连续奇数(格式：“7+9+11”);
 */
 public String GetSequeOddNum(int m)
 {
     /*在这里实现功能*/

     return null;
 }
输入描述:
输入一个int整数

输出描述:
输出分解后的string"""


while True:
    try:
        n, m= int(input()), []
        d = n**2 - n + 1
        for i in range(n):
            m.append(str(d))
            d += 2
        print('+'.join(m))
    except:
        break