n = int(input())
flower = list()

for _ in range(n):
    date = list(map(int, input().split()))
    flower.append([date[0] * 100 + date[1], date[2] * 100 + date[3]])
    
flower.sort()

cnt = 0
# 꽃이 지는 날짜 저장
end = 0 
# 마지막 꽃이 지는 날
target = 301

while flower:
    # 꽃이 지는 날이 12월 1일보다 클 경우, 3월1일 이후에 꽃이 필 경우 break
    if target >= 1201 or target < flower[0][0]:
        break
    for _ in range(len(flower)):
        if target >= flower[0][0]:
            if end <= flower[0][1]:
                end = flower[0][1]
            # 확인한 날짜는 없앰
            flower.remove(flower[0])
        # 꽃이 지는 날이 제일 빨리 피는 꽃보다 작으면 break
        else:
            break
    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
    