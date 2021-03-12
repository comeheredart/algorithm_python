#https://www.acmicpc.net/problem/1003
n = int(input())


for i in range(n):
  zero = [1, 0, 1, 1]
  one = [0, 1, 1, 2]

  now = int(input())

  if now > 3:
    
    for i in range(4,now+1):
      zero.append(zero[i-1] + zero[i-2])
      one.append(one[i-1] + one[i-2])


  print(zero[now], one[now])
  
