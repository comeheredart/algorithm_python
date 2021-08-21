#https://www.acmicpc.net/problem/2583


import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
            cnt += 1
            dfs(nx, ny)

M, N, K = map(int, input().split())

visited = [[0] * N for _ in range(M)]

for _ in range(K):
    sc, sr, ec, er = map(int, input().split())
    for i in range(sr, er):
        for j in range(sc, ec):
            visited[i][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 1 
area = 0 
ans = []

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            area += 1
            dfs(i, j)
            ans.append(cnt)
            ans = 1 

ans.sort()
print(area)
print(' '.join(map(str, ans)))