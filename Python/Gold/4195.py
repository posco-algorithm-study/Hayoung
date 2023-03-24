def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y
    
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parents[y] = x
        number[x] += number[y]
        
n = int(input())

for _ in range(n):
    parents = dict()
    number = dict()
    
    f = int(input())
    
    for _ in range(f):
        a, b = input().split(" ")
        
        if a not in parents:
            parents[a] = a
            number[a] = 1
            
        if b not in parents:
            parents[b] = b
            number[b] = 1
            
        union(a, b)
        print(number[find(a)])