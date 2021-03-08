n = int(input())


def cal(x, y):
  if y > x:
    x, y = y, x
    
  while y != 0:
    x = x % y
    x, y = y, x
    
  return x
  
for _ in range(n):
  a, b = map(int, input().split())
  print(a*b // cal(a, b))

