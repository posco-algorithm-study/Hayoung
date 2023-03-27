import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n = int(input())
parent = [0] * (n+1)
star = [(0, 0)] * (n+1)
edge = []
result = 0

for i in range(1, n+1):
    parent[i] = i
    
for i in range(1, n+1):
    x, y = map(float, input().split())
    star[i] = (x, y)
    
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)
        edge.append((cost, i, j))

edge.sort()

for k in edge:
    cost, a, b = k
    
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(round(result, 2))