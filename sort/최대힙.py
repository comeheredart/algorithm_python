import heapq
import sys

heap = []

N = int(input())

for _ in range(N):
  temp = int(sys.stdin.readline())

  if temp == 0:
    if not heap:
      print("0")
    else:
      result = heapq.heappop(heap)
      print(-result)
  else:
    heapq.heappush(heap, -temp)
