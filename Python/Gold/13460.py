from collections import deque

n, m = map(int, input().split()) 

a = [list(input().strip()) for _ in range(n)]
q = []  # bfs : queue 활용
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def init():
    rx, ry, bx, by = 0, 0, 0, 0 # 초기화
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j
                
    q.append((rx, ry, bx, by, 1))
    check[rx][ry][bx][by] = True
        
def move(x, y, dx, dy):
    cnt = 0
    
    while a[x+dx][y+dy] != '#' and a[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    init()
    while q:
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:
            break
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            
            if a[nbx][nby] != 'O':
                if a[nrx][nry] == 'O':
                    print(depth)
                    return
                
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                        
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not check[nrx][nry][nbx][nby]:
                    check[nrx][nry][nbx][nby] = True
                    
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)

solve()