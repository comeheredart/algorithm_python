#https://www.acmicpc.net/problem/1436
#화난ㄷㅏ ........
# 
n = int(input())

cnt = 0
ans = 666

while True:
  if '666' in str(ans):
    cnt += 1
  
  if cnt == n:
    print(ans)
    break

  ans += 1