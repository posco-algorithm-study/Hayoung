n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

cnt = {}

# 숫자카드와 개수를 딕셔너리에 담기
for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_list:
    if i in cnt: 
        print(cnt[i], end = ' ') # 존재하는 숫자 카드라면
    else:
        print(0, end = ' ')      # 존재하지 않는 숫자 카드라면

# n_list => 6 3 2 10 10 10 10 -10 -10 7 3
# {6:1, 3:2, 2:1, 10:3, -10:2, 7:1} 로 담긴다.