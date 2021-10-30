#https://www.acmicpc.net/problem/1520 내리막길
#단순 dfs 했더니 시간초과 -> visited로 방문처리해서 계속 방문해서 그런듯
#dfs + dp

from sys import stdin

m, n = map(int, stdin.readline().split())
M = [list(map(int, stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for i in range(m)]
#dp[i][j] M[][] 


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
  if x == m - 1 and y == n - 1:
    return 1

  if dp[x][y] == -1:
    dp[x][y] = 0
    
    for i in range(3):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if M[nx][ny] < M[x][y]:
          dp[x][y] += dfs(nx, ny)

  return dp[x][y]

print(dfs(0, 0))
