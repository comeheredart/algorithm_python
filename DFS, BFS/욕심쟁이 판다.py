#https://www.acmicpc.net/problem/4811 알약
#https://www.acmicpc.net/problem/1937 욕심쟁이 판다
#https://www.acmicpc.net/problem/1520 내리막길

# n = int(input())

# graph = []
# for i in range(n): 
#   graph.append(list(map(int, input().split())))

# visited = [[0] * n for _ in range(n)]
# dp = [[0] * n for _ in range(n)]

# ans = 0


# dx = [-1, 1, 0, 0] #상하좌우
# dy = [0, 0, -1, 1]

# def dfs(x, y):
#   global dp
#   if visited[x][y] == 0:
#     visited[x][y] = 1

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]

#       if nx >= 0 or ny >= 0 or nx <= n or ny <= n or graph[nx][ny] >= graph[x][y]:
#         dp[x][y] = max(dp[x][y], dfs[nx][ny])

#     dp[x][y] += 1
      
#   return dp[x][y]
    
  


# for i in range(n):
#   for j in range(n):
#     ans = max(ans, dfs(i, j))



# print(ans)

