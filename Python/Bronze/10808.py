from string import ascii_lowercase

s = list(map(str, input()))
s.sort()

alpha_list = list(ascii_lowercase)

# print(s)
# print(alpha_list)

for i in range(len(alpha_list)):
    y = s.count(alpha_list[i])
    print(y, end = ' ')    