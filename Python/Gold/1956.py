import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
dist = [[INF]*(v+1) for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dist[a][b] = min(c, dist[a][b])
    
for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            dist[a][b] = min(dist[a][b], dist[a][k]+dist[k][b])

ans = INF    
for i in range(1, v+1):
    ans = min(ans, dist[i][i])

if ans == INF:
    print(-1)
else:
    print(ans)

