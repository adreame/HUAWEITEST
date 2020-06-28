"""题目描述
公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，
鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
详细描述：
接口说明
原型：
int GetResult(vector &list)
输入参数：
        无
输出参数（指针指向的内存区域保证有效）：
    list  鸡翁、鸡母、鸡雏组合的列表
返回值：
     -1 失败
     0 成功
输入描述:
输入任何一个整数，即可运行程序。"""



while True:
    try:
        n, s = input(), []
        for x in range(0, 13):
            for y in range(0,26):
                if (100-5*x-3*y)*3 == 100-x-y:
                    s.append('{} {} {}'.format(x, y, 100-x-y))
        for i in s:
            print(i)
    except:
        break