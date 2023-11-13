n = int(input())
arr = []
ans = []

for _ in range(n):
    arr.append(int(input()))
    
arr.sort()

for i in range(n):
    a = arr[i] * (n-i)
    ans.append(a)
    
print(max(ans))