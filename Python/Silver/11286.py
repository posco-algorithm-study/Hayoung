import heapq
import sys

n = int(sys.stdin.readline())

hq = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(hq, (abs(x),x))
        
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])