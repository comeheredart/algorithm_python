
def solution(a):
  count = float('inf')
  str_common = a[0]

  for item in a:
    temp_count = 0
    for i in range(len(str_common)):
      if item[i] == str_common[i]:
        temp_count += 1
    
    count = min(temp_count, count)

  str_result = str_common[0:count]

  for item in a:
    for i in range(len(str_result)):
      if str_result[i] != item[i]:
        return 0


  return count

print(solution(['abcd', 'abce', 'abchg', 'abcfwqw', 'abcdfg'])) # 3
print(solution(['abcd', 'gbce', 'abchg', 'abcfwqw', 'abcdfg'])) # 0