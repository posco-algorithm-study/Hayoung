n = int(input())

stack = []
ans = []

cnt = 1
temp = True

for _ in range(n):
    a = int(input())
    
    while cnt <= a:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
        
    if stack[-1] == a:
        stack.pop()
        ans.append('-')
        
    else:
        temp = False

if temp == False:
    print("no")
    
else: 
    for i in ans:
        print(i)

    
    
    
    