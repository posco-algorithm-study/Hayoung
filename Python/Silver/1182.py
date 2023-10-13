n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0 

def back(num, sum):
    global cnt
      
    if num >= n:
        return
    sum += arr[num]
    
    if sum == s:
        cnt += 1
        
    back(num+1, sum) 
    back(num+1, sum - arr[num]) # 백트래킹
    
back(0, 0)
print(cnt)
    
    
        