n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

cnt = {}

for i in n_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_list:
    if i in cnt:
        print(cnt[i], end = ' ')
    else:
        print(0, end = ' ')
