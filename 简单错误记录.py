"""开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。 
处理:
1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；
(文件所在的目录不同，文件名和行号相同也要合并)
2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16
个字符和行号相同，也不要合并)
3.输入的文件可能带路径，记录文件名称不能带路径
输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。 文件路径为windows格式
如：E:\V1R2\product\fpgadrive.c 1325
输出描述:
将所有的记录统计并将结果输出，格式：文件名代码行数数目，一个空格隔开，如: fpgadrive.c 1325 1 结果根据数目从多
到少排序，数目相同的情况下，按照输入第一次出现顺序排序。 如果超过8条记录，则只输出前8条记录. 如果文件名的长度超
过16个字符，则只输出后16个字符
输入例子1:
E:\V1R2\product\fpgadrive.c 1325
输出例子1:
fpgadrive.c 1325 1
"""

import collections

file1 = collections.OrderedDict()  # file1字典存储文件名称与错误次数

while True:
    try:
        # 取出 fpgadrive.c 1325，作为字典的value值
        line = input().split('\\')[-1]
        # 如果之前有存储 fpgadrive.c 1325 到file1字典中
        print(line)
        if line in file1:
            file1[line] += 1
        else:
            file1[line] = 1
    except:
        break

    # 对字典按照出现次数降序排序,返回值依旧是字典
    decord = sorted(file1.items(), key=lambda d: d[1], reverse=True)

    for i in range(min(8, len(decord))):
        filename = decord[i][0].split()  # 文件名和行数作为列表的两项
        print(filename[0][-16:], filename[1], decord[i][1])
