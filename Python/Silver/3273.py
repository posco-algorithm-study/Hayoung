n = int(input())

stack = list(map(int, input().split()))
stack.sort()

x = int(input())

cnt = 0
left, right = 0, n-1

while left < right:
    temp = stack[left] + stack[right]
    if temp == x:
        cnt += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(cnt)

