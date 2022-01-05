N, M = map(int,input().split())

x, y, direction = map(int, input().split())

visited = [[0] * M for _ in range(N)]

#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[x][y] = 1


board = []
for _ in range(N):
  board.append(list(map(int, input().split())))


def turn_left():
  global direction

  direction = direction - 1

  if direction == -1:
    direction = 3
  

turn_count = 0
result = 1

while True:
  turn_left()

  nx = x + dx[direction]
  ny = y + dy[direction]


  #만약 방문 안했고 육지라면 이동
  if visited[nx][ny] == 0 and board[nx][ny] == 0:
    x, y = nx, ny

    #방문처리
    visited[x][y] = 1

    #방문칸수세기
    result += 1

    #턴 수 초기화
    turn_count = 0
    print(x, y)
    continue

  #돌아
  else:
    turn_count += 1

  #4번 돌았으면
  if turn_count == 4:
    print("들어왓음")
    #한 칸 뒤로 - 붙이면 됨
    nx = x - dx[direction]
    ny = y - dy[direction]

    print(nx, ny)
    #바다라면
    if board[nx][ny] == 0 and visited[nx][ny] == 0:
      x, y = nx, ny
      turn_time = 0

    else:
      break


print(result)