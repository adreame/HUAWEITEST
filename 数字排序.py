"""题目描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序（一组测试用例可能会有多组数据）
接口说明
原型：
void sortIntegerArray(Integer[] pIntegerArray, int iSortFlag);
输入参数：
Integer[] pIntegerArray：整型数组
int  iSortFlag：排序标识：0表示按升序，1表示按降序
输出参数：
无
返回值：
void
"""


while True:
    try:
        a,b,c = input(), list(map(int, input().split())), input()
        if c == "0":
            b.sort()
        elif c == "1":
            b.sort(reverse=True)
        print(" ".join(map(str, b)))
    except:
        break