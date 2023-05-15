from collections import deque

n = int(input())
k = int(input())
maps = [[0] * n for _ in range(n)]
for _ in range(k): # 사과 위치
    a, b = map(int, input().split())
    maps[a-1][b-1] = 1

q = []
l = int(input())
for _ in range(l): # 방향 이동 정보
    X, c = input().split()
    q.append((int(X), c))
    
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

x, y, direc, time = 0, 0, 0, 0
snake = deque([])

while True:
    snake = ((x, y)) # 뱀머리 현재 위치
    time += 1
    
    x += dx[direc]
    y += dy[direc]
    
    if x < 0 or y < 0  or x >= n or y >= n : # 벽에 부딪히면 / 자기 자신과 만나면
        break
    
    if not maps[x][y]: # 사과가 없으면
        i, j = snake.popleft()
        maps[i][j] = 0
    
    if c == "L":
        direc = (direc + 1) % 4
    else:
        direc = (direc - 1) % 4
        
print(time)   