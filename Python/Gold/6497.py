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


while True:    
    n, m = map(int, input().split())
    if m == 0 and n == 0: 
        break    
    
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
        
    edge = []
    result = 0
        
    for _ in range(m):
        a, b, c = map(int, input().split())
        edge.append((c, a, b))

    edge.sort()

    for k in edge:
        c, a, b = k
        
        if find(a) != find(b):
            union(a, b)
        else:
            result += c

    print(result)

    
    