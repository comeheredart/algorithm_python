#https://www.acmicpc.net/problem/1541

arr = input().split("-")

first = 0
ans = 0

for i in arr[0].split('+'):
  first += int(i)

ans += first

for i in arr[1:]:
  for j in i.split('+'):
    ans -= int(j)

print(ans)