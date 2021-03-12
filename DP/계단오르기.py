#https://www.acmicpc.net/problem/2579
#맨 윗칸 부터 생각하자뵤
#[10, 20, 15, 25, 10, 20]

n = int(input())
stairs = []

for _ in range(n):
  stairs.append(int(input()))

dp = [0] * (n+1)

dp[0] = stairs[0]
dp[1] = max(stairs[0], stairs[1])
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])

for i in range(3, n+1):
  dp[i] = max(stairs[i-1] + stairs[i-2] + dp[i-3], stairs[i-1] + stairs[i-3])


print(dp[n])