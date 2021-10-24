n, m = map(int, input().split())
array = list(map(int, input().split()))



def binary(array, start, end):
  answer = 0

  while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in array:
      if i > mid:
        temp += (i-mid)

    if temp >= m:
      answer = max(answer, mid)
      start = mid + 1
    else:
      end = mid - 1

  return answer


print(binary(array, 0, max(array)))