s = input().split('-')

num = []

for i in s:
    cnt = 0
    a = i.split('+')
    
    for j in a:
        cnt += int(j)
    
    num.append(cnt)
        
    n = num[0]

for i in range(1, len(num)):
    n -= num[i]
    
print(n)