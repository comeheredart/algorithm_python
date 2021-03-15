#https://www.acmicpc.net/problem/1717
# 5:23 - 5:37
#파이썬은 재귀 깊이 제한을 해줘야된다! 기억! n의 크기가 백만이니 백만으로 설정

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x


def union_parent(parent, a, b):
  ap = find_parent(parent, a)
  bp = find_parent(parent, b)

  if ap > bp:
    parent[ap] = bp
  else:
    parent[bp] = ap



n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
  parent[i] = i

for _ in range(m):
  flag, a, b = map(int, input().split())

  if flag == 0:
    union_parent(parent, a, b)
  if flag == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")

