#https://www.acmicpc.net/problem/4796

i = 1
while True:
  l, p, v = map(int, input().split())

  if l + p + v == 0:
    break

  ans = (v//p)*l

  ans += min((v%p), l)
  
  print('Case %d: %d' %(i, ans))

  i += 1
