#https://www.acmicpc.net/problem/2075 N번째 큰수
#힙에 대해 공부했다 최소 힙 최대 힙 !!! 까먹지 말자

import heapq
import sys

#길이가 N인 우선순위 큐를 만들어서 입력 받을 때 .. 이케이케하면 되지않나
N = int(input())

heap = []

for _ in range(N):
  row = list(map(int, sys.stdin.readline().split()))

  if not heap:
    for item in row:
      heapq.heappush(heap, item)

  else:
    for item in row:
      if heap[0] < item:
        heapq.heappush(heap, item)
        heapq.heappop(heap)

print(heap[0])