hour, min = map(int, input().split())
time = int(input())

if min + time >= 60:
    hour += (min + time) // 60
    min = (min + time) % 60
    if hour >= 24:
        hour -= 24
    print(hour, min)
    
else:
    min = min + time
    print(hour, min)