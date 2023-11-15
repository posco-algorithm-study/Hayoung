t = int(input())

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
        
    money = 0
    maxPrice = 0
    
    for i in range(len(stock)-1, -1, -1):
        if stock[i] > maxPrice:
            maxPrice = stock[i]
        else:
            money += maxPrice - stock[i]

    print(money)