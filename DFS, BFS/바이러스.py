#https://www.acmicpc.net/problem/2606
#입력받고, dfs로 찾아가서 visited 행렬에 없으면 넣을 때 카운트 증가시키면 답

N = int(input())
C = int(input())
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
ans = 0

#인접리스트로 입력 받기
for _ in range(C):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)


def virus(graph, visited, v):
  global ans
  visited[v] = True #방문처리하고
  
  for i in graph[v]: #들어가서
    if not visited[i]: #방문안했으면 증가시키기
      ans += 1
      virus(graph, visited, i) #이걸 재귀!
    


virus(graph, visited, 1)
print(ans)
