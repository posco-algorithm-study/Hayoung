n = int(input())

lst = []

for _ in range(n):
    start, finish = map(int, input().split())
    lst.append([start, finish])
    
lst = sorted(lst, key = lambda x : (x[1], x[0]))

cnt = 1
end_time = lst[0][1]

for i in range(1, n):
    if end_time <= lst[i][0]:
        cnt += 1
        end_time = lst[i][1]
        
print(cnt)