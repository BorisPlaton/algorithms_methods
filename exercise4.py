mas = []
answers = []
current = -1
for i in range(int(input())):
    mas.append(tuple([int(i) for i in input().split()]))
mas.sort(key=lambda x: x[1])

for elem in mas:
    if elem[0] <= current:
        continue
    else:
        current = elem[1]
        answers.append(current)

print(len(answers), *answers, sep="\n")
