#https://www.acmicpc.net/problem/7562
#DFS일거같다. 현재 위치에서 계속 움직이면서 끝까지 가는데 답이면 멈추는?

N = int(input())


dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, -2, 2, -1, 1, -2, 2]


for _ in range(N):
  can = int(input())
  x1, y1 = map(int, input().split())
  x2, y2 = map(int, input().split())


