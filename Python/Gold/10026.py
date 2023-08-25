import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[y][x] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx <n and 0 <= ny < n and graph[y][x] == graph[ny][nx] and visited[ny][nx] == False:
                dfs(nx, ny)
            
answer = 0    
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            answer += 1
            dfs(j, i)
            
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
            
            
visited = [[False] * n for _ in range(n)]
answer_2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            answer_2 += 1
            dfs(j, i)

print(answer, answer_2)
