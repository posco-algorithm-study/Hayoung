import sys
import collections
from collections import deque

n = int(sys.stdin.readline())
# queue = deque([i for i in range(1, n+1)])


# while len(queue) > 1:
#     queue.popleft()
#     queue.rotate(-1)
    
# print(queue[0])    

queue = deque([])

for i in range(1, n+1):
    	
	queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)
	        
print(queue[0])