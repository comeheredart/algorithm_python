#https://www.acmicpc.net/problem/2751
#삽입정렬! 시간복잡도는 N제곱인데 삽입정렬은 거의 정렬되어있는 상황에서 제일 강력한 알고리즘이라ㄱㅗ 한

n = int(input())
arr = []

for _ in range(n):
  arr.append(int(input()))


for i in range(1, len(arr)):
  for j in range(i, 0, -1):
    if arr[j] < arr[j-1]:
      arr[j], arr[j-1] = arr[j-1], arr[j]
    else:
      break


print(arr)


1 5 6 7 4 9 2



