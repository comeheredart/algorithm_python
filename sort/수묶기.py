#https://www.acmicpc.net/problem/1744
#1. 뒤부터묶기 2. 1은ㄴ더하기 3. 0이하 두개면 곱하기

n = int(input())
arr = []
ans = 0

for _ in range(n):
  arr.append(int(input()))
arr.sort()


for i in range(len(arr)-1, -1, -2):
  if i == 0: #하나 남았ㅅ을때 인덱스 에러 방지
    ans += arr[i]
    break
  if arr[i] > 1 and arr[i-1] > 1: #둗개다 1보다 크면
    ans += arr[i] * arr[i-1]
  elif arr[i] < 0 and arr[i-1] < 0: #두개다 0보다 작으면
    ans += arr[i] * arr[i-1]
  else:                             #그 이외 케이스
    ans += arr[i] + arr[i-1]


print(ans)