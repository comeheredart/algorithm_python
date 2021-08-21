#https://www.acmicpc.net/problem/1922
#네트워크 연결. 최소 스패닝 트리 문제

#재귀로 부모 찾기
def find(x):
   if x == parent[x]:
      return x
   parent[x] = find(parent[x])
   return parent[x]

#합치기
def union(x,y):
   x, y = find(x), find(y)
   parent[x] = y


N = int(input())
M = int(input())
distance = [list(map(int,input().split())) for _ in range(M)]
distance = sorted(distance, key=lambda k: k[2])
#간선 길이 기준 정렬

parent =[i for i in range(0,N+2)]
#부모 배열

ans = 0

for item in distance:
   start, end, weight = item

   #사이클 확인
   if find(start) == find(end):
      continue
   else:
      ans += weight
      union(start,end)
      
print(ans)