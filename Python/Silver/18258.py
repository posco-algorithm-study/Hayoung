import sys
import collections
from collections import deque

n = int(sys.stdin.readline())

queue = deque([])

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]
    
    if order == "push":
        queue.append(word[1])
        
    elif order == "pop":
        if not queue:
            print("-1")
        else:
            print(queue.popleft())
    
    elif order == "size":
        print(len(queue))
    
    elif order == "empty":
        if not queue:
            print("1")
        else:
            print("0")
            
    elif order == "front":
        if not queue:
            print("-1")
        else:
            print(queue[0])
    
    elif order == "back":
        if not queue:
            print("-1")
        else:
            print(queue[-1])      
