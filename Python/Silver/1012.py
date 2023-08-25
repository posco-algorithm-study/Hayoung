import sys
input = sys.stdin.readline
MAX = 50 + 10


# visited 배열을 활용한 정석 풀이

dx = [-1, 1, 0, 0] # ROW
dy = [0, 0, -1, 1] # COLOMN

# (0, 0)부터 시작하면 내 현재 인덱스가 -1은 아닌지 전체 가로세로 크기보다 
# 더 커지진 않았는지 매번 확인해야함 (1,1)에서 시작함으로써 겉의 테두리를 얻게된다. 
def dfs(y, x):
    global visited
    visited[y][x] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if graph[ny][nx] and not visited[ny][nx]:
            dfs(ny, nx) 

# 0. 입력 및 초기화

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프 정보 입력
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True  # (0,0) -> (1,1) 하기 위해서
        # 코드가 간결해지고 수행 속도가 빨라진다. 
        
    # 2. 방문하지 않은 지점부터 dfs 돌기
    
    answer = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)

# # graph 배열만 활용한 풀이

# # graph의 배추를 삭제한다. 1 -> 0
# # visited 배열을 활용하면 공간복잡도가 늘어난다.

# dx = [-1, 1, 0, 0] # ROW
# dy = [0, 0, -1, 1] # COLOMN

# def dfs(y, x):
#     graph[y][x] = False
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if graph[ny][nx]:
#             dfs(ny, nx) 

# # 0. 입력 및 초기화

# t = int(input())
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     graph = [[False] * MAX for _ in range(MAX)]
   
#     # 1. 그래프 정보 입력
    
#     for _ in range(k):
#         x, y = map(int, input().split())
#         graph[y + 1][x + 1] = True  # (0,0) -> (1,1) 하기 위해서
#         # 코드가 간결해지고 수행 속도가 빨라진다. 
        
#     # 2. 방문하지 않은 지점부터 dfs 돌기
    
#     answer = 0
#     for i in range(1, n+1):
#         for j in range(1, m+1):
#             if graph[i][j]:
#                 dfs(i, j)
#                 answer += 1
                
#  # if문 복잡도 내려가고 공간복잡도도 내려간다.