n, m = map(int, input().split())

boards = []
for _ in range(n):
    boards.append(list(map(int, input().split())))
    
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

def turn(dir):
    