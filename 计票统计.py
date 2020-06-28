"""题目描述
请实现接口：

unsigned int  AddCandidate (char* pCandidateName);
功能：设置候选人姓名
输入： char* pCandidateName 候选人姓名
输出：无
返回：输入值非法返回0，已经添加过返回0 ，添加成功返回1



Void Vote(char* pCandidateName);
功能：投票
输入： char* pCandidateName 候选人姓名
输出：无
返回：无

unsigned int  GetVoteResult (char* pCandidateName);

功能：获取候选人的票数。如果传入为空指针，返回无效的票数，同时说明本次投票活动结束，释放资源
输入： char* pCandidateName 候选人姓名。当输入一个空指针时，返回无效的票数

输出：无
返回：该候选人获取的票数

void Clear()
// 功能：清除投票结果，释放所有资源
// 输入：
// 输出：无
// 返回

输入描述:
输入候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票。

输出描述:
每行输出候选人的名字和得票数量。"""


from collections import Counter
while True:
    try:
        a, b, c, d, valid = input(), input().split(), input(), input().split(), 0
        cc = Counter(d)
        for i in b:
            print(i + " : " + str(cc[i]))
            valid += cc[i]
        print("Invalid : " + str(len(d)-valid))
    except:
        break