import heapq
import sys

n = int(input())

hp = []

for _ in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(hp, -x)
        
    else:
        if len(hp) == 0:
            print(0)
        else:
            print(heapq.heappop(hp)*(-1))