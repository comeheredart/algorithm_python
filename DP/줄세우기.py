#https://www.acmicpc.net/problem/2631

#bfs? dfs?
#DP래 .... 왜...?왜????????
#가장 긴 증가하는 부분 수열

n = int(input())
arr = []

for i in range(n):
  arr.append(int(input()))


dp = [0 for _ in range(n)]

dp[0] = 1
#이게 현재까지의 가장 긴 증가하는 애들인거임 ㅇㅋㅇㅋ

cur_max = 0

#이제 쭉가면서 비교해보면서 갱ㅇ신해
for cur in range(1, n):
  dp[cur] = 1
  for post in range(0, cur):
    if arr[cur] > arr[post]:
      dp[cur] = max(dp[cur], dp[post] + 1)



print(n - max(dp))
