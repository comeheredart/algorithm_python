#https://www.acmicpc.net/problem/1753
#다익스트라!
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

#입력
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


#방문 안 한 노드중에서 가장 거리가 짧은 노드 반환
def get_smallest():

  min_val = INF
  index = 0

  for i in range(1, n+1):
    if distance[i] < min_val and not visited[i]:
      index = i
      min_val = distance[i]
  
  return index

#가장 짧은 노드 들어가서 연결된 애들 보고 distance 갱신
def dijkstra(start):
  
  distance[start] = 0
  visited[start] = True

  for i in graph[start]:
    distance[i[0]] = i[1]

  for i in range(n-1):
    now = get_smallest()
    visited[now] = True
    

    for j in graph[now]:
      cost = distance[now] + j[1]
      
      if distance[j[0]] > cost:
        distance[j[0]] = cost


dijkstra(start)


for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])