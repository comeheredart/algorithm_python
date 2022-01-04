
location = input()

moves = [(1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1)]

x = int(location[1]) - 1
y = ord(location[0]) - ord('a')

result = 0

for move in moves:
  nx = x + move[0]
  ny = y + move[1]

  if nx < 0 or ny < 0 or nx > 8 or ny > 8:
    continue
  
  result += 1

print(result)