n = int(input())

for _ in range(n):
    a, b = input().split()
    lst = sorted(a)
    lst1 = sorted(b)
    
    if lst == lst1:
        print("Possible")
    else:
        print("Impossible")



