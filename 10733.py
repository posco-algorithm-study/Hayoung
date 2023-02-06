n = int(input())

lst = []

for _ in range(n):
    a = int(input())
    
    if a != 0:
        lst.append(a)
    
    else:
        lst.pop()

print(sum(lst))
    