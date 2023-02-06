n, money = map(int, input().split())

coin = []

for _ in range(n):
    coin.append(int(input()))
    
coin.sort(reverse = True)

cnt = 0

for i in coin:
    if i <= money:
        cnt += money // i
        money %= i
        
    if money == 0:
        break

print(cnt)

