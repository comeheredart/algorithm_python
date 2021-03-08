#https://www.acmicpc.net/problem/10989
#계수정렬. 임현우란테 스포당함! 시간복잡도는 O(N+K), 데이터 범위가 한정되어있으면 현존하는ㄴㅇ라고리즘 중에 제일 빠르ㄷ 근데 데이터가 0, 99999 2개만 있는 경우에도 100000 까지 배열선언해야된,까 공간복잡도에서 비효율적일수도 그랴서 동일한 값을 가지는 ㄷ이터가 여러개일 때 좋응

import sys

n = int(input())
count = [0 for _ in range(10001)]

for _ in range(n):
  i = int(sys.stdin.readline())
  count[i] += 1


for i in range(10001):
  if count[i] != 0:
    for _ in range(count[i]):
      print(i)


