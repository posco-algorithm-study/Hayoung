n = int(input())

lst = list(map(int, input().split()))
    
lst.sort()

num = 0
time = []

for i in lst:
    num += i
    time.append(num)
    
print(sum(time))
    