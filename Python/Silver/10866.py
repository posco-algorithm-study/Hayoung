import sys
import collections
from collections import deque

n = int(input())
dq = deque([])

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]
    
    if order == "push_front":
        dq.appendleft(word[-1])
    
    elif order == "push_back":
        dq.append(word[-1])
    
    elif order == "pop_front":
        if not dq:
            print(-1)
        else:
            print(dq[0]) 
            dq.popleft()
    
    elif order == "pop_back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])
            dq.pop()
            
    elif order == "size":
        print(len(dq))
    
    elif order == "empty":
        if not dq:
            print(1)
        else:
            print(0)
    
    elif order == "front":
        if not dq:
            print(-1)
        else:
            print(dq[0])
    
    elif order == "back":
        if not dq:
            print(-1)
        else:
            print(dq[-1])