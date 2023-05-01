n = int(input())

a = list(map(int, input().split()))

b, c = map(int, input().split())

count = n

for i in a:
    i -= b
    
    if i > 0:
        if i % c >= 1:
            count += (i // c) + 1
        else:
            count += i // c

print(count)
