#https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())

# 재귀
# def GCD(x, y):
#   if y == 0:
#     return x
#   return GCD(y, x%y)

def GCD(x, y):
  if x < y:
    x, y = x, y

  while y!=0:
    x = x%y
    x,y = y,x

  return x

print(GCD(a,b), a*b//GCD(a,b))
