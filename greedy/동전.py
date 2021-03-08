#https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())

arr = []
count = 0

for _ in range(N):
  arr.append(int(input()))

arr.sort(reverse=True)

while True:
  for i in arr:
    if i <= K:
      K -= i
      count += 1
      break

  if K == 0:
    break


print(count)