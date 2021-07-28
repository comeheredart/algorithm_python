#https://www.acmicpc.net/problem/2143
#부분합구하고 투 포인터로 해결

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

#부분합 구하기
partA = []
partB = []

for i in range(n):
  sum = 0
  for j in range(i, n):
    sum += A[j]
    partA.append(sum)

for i in range(m):
  sum = 0
  for j in range(i, m):
    sum += B[j]
    partB.append(sum)


partA.sort()
partB.sort(reverse=True)

#print(partA)
#print(partB)

#투 포인터 사용, 카운트 세기
ans = 0

lenA = len(partA)
lenB = len(partB)

pa = 0
pb = 0


while pa < lenA and pb < lenB:
  sum = partA[pa] + partB[pb]
  
  if sum == t:
    tempA = partA[pa]
    tempB = partB[pb]
    tempCntA = 0
    tempCntB = 0

    while pa < lenA and partA[pa] == tempA:
      pa += 1
      tempCntA += 1

    while pb < lenB and partB[pb] == tempB:
      pb += 1
      tempCntB += 1

    ans += tempCntA * tempCntB

  elif sum > t:
    pb += 1
  
  elif sum < t:
    pa += 1


print(ans)
  
  
  

      
