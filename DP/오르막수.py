#https://www.acmicpc.net/problem/11057

n = int(input())

table = [[0] * 10 for i in range(n+1)]

def fill(table, n):

  if n == 1:
    return 10

  for i in range(10):
    table[1][i] = i

  first = 10
  for i in range(10):
    table[2][i] = first
    first -= 1


  for i in range(3, n+1):
    for j in range(10):
      for k in range(j,10):
        table[i][j] += table[i-1][k]

  return sum(table[n])
  

print(fill(table, n) % 10007)