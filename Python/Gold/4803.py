import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(x, y):
    visited[x] = True
    for i in graph[x]:
        if i == y:
            continue
        if visited[i]:
            return False
        if not dfs(i, x):
            return False
    return True

answer = 0
cnt = 0

while True:
    n, m = map(int, input().split())
    cnt += 1
    answer = 0
    
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if visited[i]:
            continue
        if dfs(i, 0):
            answer += 1
            
    if answer == 0:
        print("Case {}: No trees.".format(cnt))
    elif answer == 1:
        print("Case {}: There is one tree.".format(cnt))
    else:
        print("Case {}: A forest of {} trees.".format(cnt, answer))