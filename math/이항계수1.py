# nCr = n-1Cr-1 + n-1Cr
#재귀로 하는 방법
a,b = map(int, input().split())

def two(a, b):
  if a == b or b == 0:
    return 1
  
  else:
    return two(a-1, b-1) + two(a-1, b)


print(two(a, b))