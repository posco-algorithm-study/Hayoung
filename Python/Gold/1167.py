import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# dfs 탐색
def dfs(x, y):
    # 각 노드와 연결된 노드를 확인
    for a, b in graph[x]:
        if visited[a] == -1:
            visited[a] = b + y
            dfs(a, b + y)
            
n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n):
    w = list(map(int, input().split()))
    for j in range(1, len(w)-2, 2):
        graph[w[0]].append([w[j], w[j+1]])

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))
visited = [-1] * (n+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))

    