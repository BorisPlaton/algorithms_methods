f_word = input()
s_word = input()
mas = []

for l, i in enumerate(range(len(s_word) + 1)):
    if not l:
        mas.append([i for i in range(len(f_word) + 1)])
    else:
        mas.append([l] + [-1 for i in range(len(f_word))])

for i in range(len(s_word)):
    for j in range(len(f_word)):
        c = 0 if f_word[j] == s_word[i] else 1
        mas[i + 1][j + 1] = min([mas[i][j + 1] + 1, mas[i + 1][j] + 1, mas[i][j] + c])

print(mas[len(s_word)][len(f_word)])
