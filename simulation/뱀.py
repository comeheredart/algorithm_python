#https://www.acmicpc.net/problem/3190
#시뮬레이션인거같다!

N = int(input())
K = int(input())
mapdata = [[0] * (N+1) for _ in range(N+1)]
spin = []

for _ in range(K):
  x, y = map(int, input().split())
  mapdata[x][y] = 1

r = int(input())
for _ in range(r):
  x, y = input().split()
  spin.append((int(x), y))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, r):
  if r == "L":
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4

def simulate():
  x, y = 1, 1
  mapdata[x][y] = 100
  direction = 0
  time_past = 0
  index = 0
  q = [(x, y)]

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= N and 1 <= ny and ny <= N and mapdata[nx][ny] != 100:
      if mapdata[nx][ny] == 0:
        mapdata[nx][ny] == 100
        q.append((nx, ny))
        px, py = q.pop(0)
        mapdata[px][py] = 0

      if mapdata[nx][ny] == 1:
        mapdata[nx][ny] == 100
        q.append((nx, ny))

    else:
      time_past += 1
      break
      
    x, y = nx, ny
    time_past += 1

    if index < 1 and time_past == spin[index][0]:
      direction = turn(direction, spin[index][1])
      index += 1

  return time_past

print(simulate())
