n, m = map(int, input().split())
arr = []

def back():
    if len(arr) == m: # 배열의 길이 확인
        print(" ".join(map(str, arr))) # 각 수열을 공백으로 구분해서 출력하기 위해
        return
    for i in range(1, n+1):
        if i not in arr: # 중복 확인
            arr.append(i) # 배열 추가
            back()
            arr.pop() # return으로 돌아오면 실행. 1, 2, 3 일 때 3을 없앰으로 전 단계로 돌아가는 것
back()

# from itertools import permutations
# n, m = map(int, input().split())
# p = permutations(range(1, n+1), m)
# for i in p:
#     print(" ".join(map(str, i)))