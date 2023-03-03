import sys

input = sys.stdin.readline

n, c = map(int, input().split())

hs = []
for _ in range(n):
    hs.append(int(input()))
hs.sort()

start = 1
end = hs[n-1] - hs[0]
result = 0

if c == 2: # 집이 2개라면 무조건 처음, 마지막 집 사이의 거리
    print(end)

else:
    while start < end:
        mid = (start + end) // 2

        cnt = 1 # 첫 집은 무조건 설치하니까
        ts = hs[0] # 마지막으로 공유기 설치된 위치 저장
        
        for i in range(n):
            if hs[i] - ts >= mid:
                cnt += 1
                ts = hs[i]
        
        if cnt >= c:
            result = mid
            start = mid + 1
        
        else:
            end = mid
    print(result)


    