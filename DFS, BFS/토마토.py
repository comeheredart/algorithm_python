#https://www.acmicpc.net/problem/7576
#도마도. BFS! 1인 애 상하좌우 보면서 만약 0이면 1로 바꾸고, 안되면 -1 출력...
#BFS는 큐로 구현. 큐에 1인 자식넣고 그 주위 애가 0이면 바꾸고 걔를 큐에 넣고 이런 식

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(M):
  graph.append(list(map(int, input().split())))


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]



def tomato(graph):
  queue = deque()
  ans = 0

  #처음에 1인 애 큐에 넣기
  for i in range(M):
    for j in range(N):
      if graph[i][j] == 1:
        queue.append((i, j))


  while queue:

    for i in range(len(queue)):
      x, y = queue.popleft()

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= M or ny >= N:
          continue

        if graph[nx][ny] == 0: #안 익었으면 익히고, 큐에 넣는다
          graph[nx][ny] = 1
          queue.append((nx, ny))
      
    ans += 1

  #안 익은 애 발견하면 불가능한거
  for i in range(M):
      for j in range(N):
        if graph[i][j] == 0:
          return -1
        
  return ans - 1


print(tomato(graph))
