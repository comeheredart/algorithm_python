

K = int(input())
stack = []
ans = 0

for i in range(K):
  now = int(input())

  if now == 0:
    top = stack.pop()
    ans = ans - top
  else:
    stack.append(now)
    ans = ans + now



print(ans)
