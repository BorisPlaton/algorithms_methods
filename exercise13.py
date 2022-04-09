input()
mas = [int(i) for i in input().split()]
minimal = min(mas)
maximum = max(mas)
sup = [0 for i in range(maximum - minimal + 1)]

for i in mas:
    sup[i-minimal] += 1

mas.clear()
for index, num in enumerate(sup):
    if num:
        for i in range(num):
            mas.append(index+minimal)

print(*mas)