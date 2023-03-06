import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [[INF]*(n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            dist[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(c, dist[a][b])
            

# Floyd-Warshall Algorithm
for k in range(1, n+1):         # 거치는 점
    for a in range(1, n+1):     # 시작점
        for b in range(1, n+1): # 끝점
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if dist[a][b] == INF:
            print('0', end = ' ')
        else:
            print(dist[a][b], end = ' ')
    print()
