import math

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
star = [(0, 0)] * (n+1)
    
edge = []
result = 0

for i in range(1, n+1):
    x, y = map(int, input().split())
    star[i] = (x, y)

for i in range(m):
    a, b = map(int, input().split())
    union(a, b)
    
for i in range(1, n+1):
    for j in range(i+1, n+1):
        cost = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)
        edge.append((cost, i, j))
        
edge.sort()

for k in edge:
    cost, a, b = k
    
    if find(a) != find(b):
        union(a, b)
        result += cost

print('%.2f'%(result))
    