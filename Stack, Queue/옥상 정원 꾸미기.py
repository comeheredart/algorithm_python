#https://www.acmicpc.net/problem/6198
#옥상정원꾸미기. 브루트포스로 하면 시간초과가 난다. 스택을 이용해서 풀어라??

N = int(input())
h = [int(input()) for _ in range(N)]


stack, ans = [], 0

for i in range(N):
  while stack != [] and stack[-1] <= h[i]:
    stack.pop()
  stack.append(h[i])
  ans += len(stack) - 1


print(ans)