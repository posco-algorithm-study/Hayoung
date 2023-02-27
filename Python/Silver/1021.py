from collections import deque

n, m = map(int, input().split())
position = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

count = 0
for i in position:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2: # 뽑아내려는 수의 위치 인덱스가 dq의 길이를 반으로 나눈것보다 작을 때는 왼쪽으로 움직여야 최소
                while dq[0] != i: # dq의 첫번째 인덱스가 i와 같아질때까지 반복
                    dq.append(dq.popleft())
                    count += 1
            
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1
print(count)

