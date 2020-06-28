"""题目描述
从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值，结果保留一位小数，如果没有非负数，则平均值为0
本题有多组输入数据，输入到文件末尾，请使用while(cin>>)读入
输入描述:
输入任意个整数
输出描述:
输出负数个数以及所有非负数的平均值"""


while True:
    try:
        nums = input().split()
        n = 0
        m = 0
        for i in nums:
            if int(i)<0:
                n = n+1
            else:
                m = m + int(i)
        print(n)
        print(round(m/(len(nums)-n),1))
    except:
        break