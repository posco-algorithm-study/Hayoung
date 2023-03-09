import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())

tree = [[] for _ in range(n+1)]
parent = [None for _ in range(n+1)]

def dfs(graph, root, visited):
    for i in graph[root]:
        if not visited[i]:
            visited[i] = root
            dfs(graph, i, visited)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
dfs(tree, 1, parent)

for i in range(2, n+1):
    print(parent[i])