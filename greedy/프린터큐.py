#https://www.acmicpc.net/problem/1966

#큐를 사용하는 문제
#알고 싶은거 표시해두고 만약 맨앞이 최대값이면 카운트 증가, 걔가 표시한 애면 출력, 아니면 넘어가

testcase = int(input())

for _ in range(testcase):
  n, wonder = map(int, input().split())
  priority = list(map(int, input().split()))
  checkList = [0] * n
  checkList[wonder] = 1

  count = 0

  while True:
    if priority[0] == max(priority):
      count += 1

      if checkList[0] == 1:
        print(count)
        break

      else:
        del priority[0]
        del checkList[0]


    else:
      priority.append(priority[0])
      checkList.append(checkList[0])

      del priority[0]
      del checkList[0]
      
      
      

  