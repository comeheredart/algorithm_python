#https://www.acmicpc.net/problem/5052
#리스트 정렬한 다음 겹치는지 아닌지 보면 될ㄹ가?
#sys쓸땐 input쓰지말자...

import sys

def check(arr):
  for i in range(len(arr)-1):
    length = len(arr[i])
    nxt = arr[i+1]

    if nxt[0:length] == arr[i]:
      return 0

  return 1


num = int(sys.stdin.readline())

for i in range(num):
  n = int(sys.stdin.readline())
  arr = []

  for _ in range(n):
    arr.append(sys.stdin.readline().strip())
  
  arr.sort()

  if check(arr) == 0:
    print("NO")
  else:
    print("YES")
    