n, m = map(int, input().split())
parents = [0] * (n + 1)
for i in range(n + 1):
    parents[i] = i

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if a == b:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
for i in range(m):
    c, a, b = list(map(int, input().split()))
    if c == 0:
        union(a, b)
    elif c == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    