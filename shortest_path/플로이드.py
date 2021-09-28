#https://www.acmicpc.net/problem/1520 내리막길
#플로이드 알고리즘
INF = int(1e9)

#노드 개수
n = int(input())

#간선 개수
m = int(input())

#그래프 만들기, 모든 값 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기에서 자기자신으로 가는 값 0으로 초기화
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      graph[i][j] = 0

#간선 정보 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

#점화식으로 플로이드 수행 for 3

for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      

for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("무한", end=" ")

    else:
      print(graph[a][b], end=" ")
    
  print()




