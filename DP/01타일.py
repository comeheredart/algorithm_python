#https://www.acmicpc.net/problem/1904
#n 은 -1에다가 1붙인거랑 -2에다가 00붙인거 더 하면 됨
#메로리초과..디로리..

import sys 
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
  dp[i] = dp[i-2] + dp[i-1]


print(dp[n] % 15746)