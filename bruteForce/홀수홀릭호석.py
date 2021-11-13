#https://www.acmicpc.net/problem/20164

import sys

N = int(input())
MIN, MAX = sys.maxsize, 0

def cntOdd(n):
    cnt = 0
    odds = ['1','3','5','7','9']
    s = str(n)
    for i in s:
        if i in odds:
            cnt += 1
    return cnt

def res(n, cnt):
    global MIN, MAX
    s = str(n)
    cnt += cntOdd(n)

    if len(s) == 1:
        MIN = min(MIN, cnt)
        MAX = max(MAX, cnt)
        return

    elif len(s) == 2:
        n = n//10 + n%10
        res(n, cnt)
        
    else:
        s = str(n)
        for i in range(1, len(s)-1):
            for j in range(i+1, len(s)):
                temp = int(s[:i]) + int(s[i:j]) + int(s[j:])
                res(temp, cnt)

res(N, 0)
print(str(MIN) + ' ' + str(MAX))
