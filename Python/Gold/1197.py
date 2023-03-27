import sys

v, e = map(int, input().split())

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

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i
    
edge = []
result = 0
    
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
    
edge.sort()

for k in edge:
    c, a, b = k
    
    if find(a) != find(b):
        union(a, b)
        result += c

print(result)