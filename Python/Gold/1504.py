import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    return distance

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# v1_path = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
# v2_path = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)

    
