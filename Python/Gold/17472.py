import sys
from collections import deque
input = sys.stdin.readline

# 생성 가능한 다리 찾기
def check(li):
    start, cnt = 0, 0
    flag = False
    for idx in range(len(li)):
        if li[idx] and not flag:
            flag = True
            start = li[idx]
        elif not li[idx] and flag:
            cnt += 1
        elif li[idx] and flag and start != li[idx]:
            if start and cnt >= 2:
                if (start, li[idx], cnt) not in edge:
                    edge.append((start, li[idx], cnt))
            cnt = 0
            start = li[idx]
        elif start == li[idx]:
            cnt = 0

n, m = map(int, input().split())
island = [list(map(int, input().split())) for _ in range(n)]
numbering = 1 # 섬 고유번호
used = []  # BFS 사용 시 방문여부 판단
queue = deque([]) # BFS에서 사용하는 큐
edge = [] # 생성 가능한 다리 후보 담는 배열

# BFS 이용하여 섬 고유번호 붙이기
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    for j in range(m):
        if island[i][j] and (i, j) not in used:
            queue.append((i, j))
            used.append((i, j))
            
            while queue:
                r, c = queue.popleft()
                island[r][c] = numbering

                for idx in range(4):
                    nr = r + direction[idx][0]
                    nc = c + direction[idx][1]
                    
                    if 0 <= nr < n and 0 <= nc < m:
                        if island[nr][nc] and (nr, nc) not in used:
                            queue.append((nr, nc))
                            used.append((nr, nc))
            numbering += 1

# 행 탐색
for row in island:
    if sum(row):
        check(row)

# 열 탐색
for col in list(zip(*island)):
    if sum(col):
        check(col)
        
# kruscal algorithm 
edge = sorted(edge, key = lambda x:[x[2]])

parent = [i for i in range(numbering)]
rank = [1 for i in range(numbering)]

# 부모 찾는 함수
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

answer = 0

# 합치는 함수(grouping)
def union(a, b, c):
    global answer
    a = find(a)
    b = find(b)
    
    if a != b:
        answer += c

        if rank[a] < rank[b]:
            rank[b] += rank[a]
            parent[a] = b
        
        else:
            rank[a] += rank[b]
            parent[b] = a
            
for e in edge:
    union(e[0], e[1], e[2])

if max(rank) != numbering - 1:
    print(-1)
else:
    print(answer)
        
    