import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]

def dfs(x, weight):
    # 반복문을 통해 현재 노드와 연결된 노드, 연결된 노드의 가중치를 확인
    for i in tree[x]:
        a, b = i
        
        # 탐색하지 않은 노드라면 탐색
        if distance[a] == -1:
            distance[a] = weight + b # 이전 노드의 가중치와 현재 노드의 가중치를 더한다. 
            dfs(a, weight+b) # 재귀적으로 연결된 모든 노드를 탐색
        
    
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])
    
distance = [-1] * (n + 1) # 탐색 확인, 가중치 확인
distance[1] = 0 # 시작 노드는 가중치를 0으로 초기화
dfs(1, 0) # 첫 번째 노드를 dfs 탐색

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance)) 
distance = [-1] * (n + 1) # 탐색 확인, 가중치 확인
distance[start] = 0 # 가장 먼 노드의 가중치를 0으로 초기화
dfs(start, 0) # 가장 먼 노드를 dfs 탐색

print(max(distance)) # 트리의 지름 출력