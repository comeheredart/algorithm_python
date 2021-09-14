#https://www.acmicpc.net/problem/10816
#일단 절대 단순 반복문으로 안되겟고
#만약 리스트가 1000만 단위가 넘어가면 안된다고 생각해자
#이분탐색으로 찾아야지


N = int(input())
have = list(map(int, input().split()))

M = int(input())
doyou = list(map(int, input().split()))

ans = [0] * M

have.sort()

def find(goal, have, left, right):
  if left > right:
    return 0

  mid_index = (left+right) // 2
  mid = have[mid_index]
  
  if goal == mid:
    return have.count(goal)
  elif goal < mid:
    return find(goal, have, left, right-1)
  elif goal > mid:
    return find(goal, have, left+1, right)
  else:
    return 0
    
  

for i in range(M):
  ans[i] = find(doyou[i], have, 0, M-1)




print(ans)

  
