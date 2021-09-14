#https://www.acmicpc.net/problem/10816
#딕셔너리로 푼 방법


N = int(input())
have = list(map(int, input().split()))

M = int(input())
doyou = list(map(int, input().split()))

dic = {}

for i in have:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in doyou:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
