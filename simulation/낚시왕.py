import sys
r, c, m = map(int, sys.stdin.readline().split())

board = [0 for _ in range(c) for _ in range(r)]

for _ in range(m):
  y, x, s, d, z = map(int, sys.stdin.readline().split())
  board[y-1][x-1] = (s, d-1, z)
  

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def catch(col, board):
  size = 0
  for idx in range(len(board)):
    if board[idx][col] != 0:
      speed, di, size = board[idx][col]
      board[idx][col] = 0
      
  return size


def move(board):
    new_shark = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] != 0:
                speed, i, size = board[y][x]

                # 왔다갔다 없애기
                if i == 0 or i == 1:
                    speed %= ((2 * len(board)) - 2)
                elif i == 2 or i == 3:
                    speed %= ((2 * len(board[0])) - 2)
                
                ny, nx = y, x
                # 시작부터 방향 반대로
                if ny == 0 and i == 0:
                    i = 1
                elif ny == len(board) - 1 and i == 1:
                    i = 0
                elif nx == len(board[0]) - 1 and i == 2:
                    i = 3
                elif nx == 0 and i == 3:
                    i = 2


                # 상어 이동인데 막히면 방향바꾸고
                for _ in range(speed):
                    if i == 0:
                        ny -= 1
                        if ny - 1 < 0:
                            i = 1
                    elif i == 1:
                        ny += 1
                        if ny + 1 >= len(board):
                            i = 0
                    elif i == 2:
                        nx += 1
                        if nx + 1 >= len(board[0]):
                            i = 3
                    elif i == 3:
                        nx -= 1
                        if nx - 1 < 0:
                             i = 2


                # 이동한 지점에 상어가 없거나, 원래있던 상어보다 크기가 큰 경우
                if new_shark[ny][nx] == 0 or size > new_shark[ny][nx][2]:
                    new_shark[ny][nx] = (speed, i, size)
               
    return new_shark


shark_size = 0
for idx in range(c):
    shark_size += catch(idx, board)
    board = move(board)
print(shark_size)