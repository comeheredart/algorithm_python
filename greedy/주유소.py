#https://www.acmicpc.net/problem/13305

N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

ans = 0
min_val = price[0]

for i in range(N-1):
  if price[i] < min_val:
    min_val = min(min_val, price[i])
  ans += min_val * distance[i]


print(ans)
