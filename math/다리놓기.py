#https://www.acmicpc.net/problem/1010

from math import factorial as fac

a = [] #N
b = [] #M
c = [] #경우의 수

while True:
  try:
    t = int(input())
  except:
    continue


for x in range(t):
  num1, num2 = input().split()
  a.append(int(num1))
  b.append(int(num2))

  if a[x] > b[x]:
    c.append(0)
  elif a[x] == b[x]:
    c.append(1)
  else:
    c.append(fac(b[x])//fac(b[x]-a[x])//fac[a[x]])



for y in range(t):
  print(c[y])