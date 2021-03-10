#https://www.acmicpc.net/problem/1920
#수찾기 10-5 * 10-5 인건가??

import sys
input = sys.stdin.readline

n = int(input())
one = list(map(int, input().split()))
one.sort()

m = int(input())
two = list(map(int, input().split()))

def binary(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if array[mid] == target:
      return 1
      
    elif array[mid] > target:
      end = mid - 1
      
    else:
      start = mid + 1

  return 0


for i in two:
  result = binary(one, i, 0, n-1)

  if result == 0:
    print(0)
  else:
    print(1)
    