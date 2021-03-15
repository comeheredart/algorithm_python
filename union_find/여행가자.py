#https://www.acmicpc.net/problem/1976
#6:00 - 6:27
#같은 집합인지 확인하면 되겠다!


def find(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


def union(parent, a, b):
  ap = find(parent, a)
  bp = find(parent, b)

  if ap > bp:
    parent[ap] = bp
  else:
    parent[bp] = ap


n = int(input())
m = int(input())
graph = [0]
parent = [0] * (n+1)

#parent 리스트 초기화
for i in range(n+1):
  parent[i] = i

#그래프 입력받기
for i in range(n):
  val_input = list(map(int, input().split()))
  graph.append(val_input)

#유니온 수행
for i in range(1,n+1):
  for j in range(n):
    if graph[i][j] == 1:
      union(parent, i, j+1)

input_val = list(map(int, input().split()))

#결과 함수
def output(input_val):
  base = int(find(parent, input_val[0])) #일단 초기값으로 0번째 꺼 박아놓는다
  for i in input_val:
    if find(parent, i) != base: 
      return "NO" #다르면 안되는 경로

  return "YES" #포문 다 돌고 나와서 예스이면 되는 경로


print(output(input_val))