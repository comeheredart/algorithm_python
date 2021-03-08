#https://www.acmicpc.net/problem/11399

n = int(input())
arr = list(map(int, input().split()))
ans = 0
temp = 0

arr.sort()


for i in range(n):
  temp += arr[i]
  ans += temp

print(ans)