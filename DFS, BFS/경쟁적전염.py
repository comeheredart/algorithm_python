#https://www.acmicpc.net/problem/18405
#BFS쓰즈

from collections import deque
n, k = map(int, input().split())

graph = []
virus = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j], 0, i, j))


virus.sort()
q = deque(virus)

input_time, input_x, input_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
  now, s, x, y = q.popleft()

  if s == input_time:
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] == now
        q.append((now, s+1, nx, ny))


print(graph[input_x-1][input_y-1])