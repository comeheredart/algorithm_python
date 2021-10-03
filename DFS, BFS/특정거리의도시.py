#https://www.acmicpc.net/problem/18352 특정 거리의 도시

import sys
from sys import stdin
from collections import deque
#최단거리가 k인 도시 번호 출력

n, m, k, x = map(int, stdin.readline().split())

graph = [[] for _ in range(n+1)]
#최단거리 저장하는 배열
distance = [-1] * (n+1)
distance[x] = 0
#방문 표시와 거리표시 둘 다 해주기

#연결 간선 입력
for _ in range(m):
  a, b = map(int, stdin.readline().split())
  graph[a].append(b)

def bfs(start):
  q = deque([start])
  while q:
    v = q.popleft()
    for cur in graph[v]:
        if distance[cur] == -1:
          distance[cur] = distance[v] + 1
          q.append(cur)

bfs(x)

check = False

for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
  
