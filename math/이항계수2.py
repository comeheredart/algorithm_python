#https://www.acmicpc.net/problem/11051
#파스칼의 삼각형!!

a, b = map(int, input().split())

tri = [[0] * 1 for i in range(1002)]
tri[1].append(1)

for i in range(2, 1002):
  for j in range(1, i + 1):
    if j == 1:
      tri[i].append(1)
    elif j == i:
      tri[i].append(1)
    else:
      tri[i].append(tri[i-1][j] + tri[i-1][j-1])

print(tri[a+1][b+1] % 10007)