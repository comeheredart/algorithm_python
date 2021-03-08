#https://www.acmicpc.net/problem/7576
#도마도 3차원.

from collections import deque

Y, X, H = map(int, input().split())

graph = []


for _ in range(H):
  temp = []
  graph.append(temp)
  for _ in range(X):
    temp.append(list(map(int, input().split())))



dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dz = [1, -1, 0, 0, 0, 0]

print(graph)

def tomato(graph):
  queue = deque()
  ans = 0

  #처음에 1인 애 큐에 넣기
  for z in range(H):
    for i in range(X):
      for j in range(Y):
        if graph[z][i][j] == 1:
          queue.append((z, i, j))


  while queue:

    for i in range(len(queue)):
      z, x, y = queue.popleft()

      for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
      
        if nx < 0 or ny < 0 or nz < 0 or nx >= X or ny >= Y or nz >= H:
          continue

        if graph[nz][nx][ny] == 0:
          graph[nz][nx][ny] = 1
          queue.append((nz, nx, ny))
          print(queue)
    
    ans += 1

    for z in range(H):
      for i in range(X):
        for j in range(Y):
          if graph[z][i][j] == 0:
            return -1
        
  return ans - 1


print(tomato(graph))
