import sys

k, n = map(int, sys.stdin.readline().split())
lan = []

for _ in range(k):
    lan.append(int(sys.stdin.readline()))
    
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    
    lines = 0 # 랜선 수 
    
    for i in lan:
        lines += i // mid # 분할 된 랜선 수
    
    if lines >= n: # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1

print(end)