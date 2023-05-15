n, m, x, y, k = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
      
c = list(map(int, input().split()))
    
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    
    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, d
    
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
        
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
        
for i in c:
    x += dx[i-1]
    y += dy[i-1]
    
    if x < 0 or y < 0 or x >= n or y >= m:
        x -= dx[i-1]
        y -= dy[i-1]
        continue
    
    turn(i)
    
    if maps[x][y] == 0:
        maps[x][y] = dice[5]
        
    else:
        dice[5] = maps[x][y]
        maps[x][y] = 0
        
        
    print(dice[0])
