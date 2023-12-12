n = int(input())
num_minus = []
num_plus = []

ans = 0

for _ in range(n):
    num = int(input())
    
    if num > 1:
        num_plus.append(num)
    elif num <= 0:
        num_minus.append(num)
    else:
        ans += num

num_plus.sort(reverse = True)
num_minus.sort()

for i in range(0, len(num_plus), 2):
    if i+1 >= len(num_plus):
        ans += num_plus[i]
    else:
        ans += (num_plus[i] * num_plus[i+1])
        
for i in range(0, len(num_minus), 2):
    if i+1 >= len(num_minus):
        ans += num_minus[i]
    else:
        ans += (num_minus[i] * num_minus[i+1])
        
print(ans)