import sys
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    dist[start] = 0
    
    # n번의 라운드를 반복
    for i in range(n):
        # 매 라운드마다 모든 간선을 확인
        for j in range(m):
            now = edges[j][0]
            next = edges[j][1]
            cost = edges[j][2]
            
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[now] != INF and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost
                if i == n-1:
                    return True
    return False

n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
                