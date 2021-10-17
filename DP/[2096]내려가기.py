#https://www.acmicpc.net/problem/2096 내려가기
N = int(input())

table = [list(map(int, input().split())) for _ in range(N)]

#S[i][0] = min(S[i-1][0], S[i-1][1])
#S[i][1] = min(S[i-1][0], S[i-1][1], S[i-1][2])
#S[i][2] = min(S[i-1][1], S[i-1][2])
#메모리 초과 ...

maxArr = table[0]
minArr = table[0]

for i in range(1, N):
  maxArr = [max(maxArr[0], maxArr[1]) + table[i][0],
  max(maxArr[0], maxArr[1], maxArr[2]) + table[i][1], 
  max(maxArr[1], maxArr[2]) + table[i][2]]

  minArr = [min(minArr[0], minArr[1]) + table[i][0],
  min(minArr[0], minArr[1], minArr[2]) + table[i][1],
  min(minArr[1], minArr[2]) + table[i][2]]

  x = max(maxArr[0], maxArr[1]) + table[i][0]
  y = max(maxArr[0], maxArr[1], maxArr[2]) + table[i][1]
  z = max(maxArr[1], maxArr[2]) + table[i][2]
  
  #minArr[0] = min(minArr[0], minArr[1]) + table[i][0]
  #minArr[1] = min(minArr[0], minArr[1], maxArr[2]) + table[i][1]
  #minArr[2] = min(minArr[1], minArr[2]) + table[i][2]

print(max(maxArr))
print(min(minArr))
