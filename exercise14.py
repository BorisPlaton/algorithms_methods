n = int(input())
mas = [int(i) for i in input().split()]
indexes = [1] * n

for i in range(n):
    for j in range(i):
        if mas[j] <= mas[i] and indexes[j] + 1 > indexes[i] and mas[i] % mas[j] == 0:
            indexes[i] = indexes[j] + 1

print(max(indexes))
