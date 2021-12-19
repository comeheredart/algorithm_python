import sys
input = sys.stdin.readline

#레이저 방향 변환 함수
def find_direction(x_, y_):
    x, y = x_, y_
    
    if x == 0:
        return 2
    elif x == n + 1:
        return 0
    elif y == 0:
        return 1
    elif y == n + 1:
        return 3
 
#레이저 이동 재귀함수
def move_laser(start, direction):
    global out_x, out_y
    x, y = start
    x, y = x + dx[direction], y + dy[direction] 
    
    #밖으로
    if x in (0, n + 1) or y in (0, n + 1):
        out_x, out_y = str(x), str(y)
        return
    
    #거울이면
    if board[x][y] != 0:
        new_direction = (direction + 1) % 4   
        #오른쪽 90도 회전
        
        #보드 값이 새 방향과 같은 경우(무한반복)
        if board[x][y] == new_direction:
            out_x, out_y = '0', '0'
            return
        
        #보드 값을 새 방향 값으로 갱신
        board[x][y] = new_direction
        direction = new_direction
    
    #다음 칸으로 이동
    move_laser((x, y), direction)
 
 

T = int(map(int, input.split()))
 
for _ in range(T):

    n, r = map(int, input.split())
    board = [[0] * (n + 2) for _ in range(n + 2)]

    #거울 위치
    for _ in range(r):
        x, y = map(int, input.split())
        board[x][y] = -1
        
    #레이저 시작, 방향
    laser = tuple(map(int, input.split()))
    laser_direction = find_direction(laser[0], laser[1])
        
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    #레이저 빔의 마지막 좌표
    out_x, out_y = -1, -1   
    
    #레이저 이동
    move_laser(laser, laser_direction)
    print(out_x + ' ' + out_y)