#https://www.acmicpc.net/problem/4811

#https://www.acmicpc.net/problem/2753

N = int(input())

def are(N): 
  if (N % 4 and N % 100 != 0) or N % 400 == 0:
    return 1
  return 0



print(are(N))