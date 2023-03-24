n = int(input())
m = int(input())
parents = [i for i in range(n)]

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
        
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] == 1:
            union(i, j)

####
parents = [-1] + parents
path = list(map(int, input().split()))
start = parents[path[0]]
for i in range(1, m):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")
    