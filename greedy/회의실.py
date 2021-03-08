n = int(input())
data = []
ans = 0

for _ in range(n):
  start, end = map(int, input().split())
  data.append((start, end))


data = sorted(data, key=lambda x:(x[1], x[0]))

time = 0
for i in data:
  if i[0] >= time:
    ans += 1
    time = i[1]

print(ans)