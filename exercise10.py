def binary(mas, element):
    left = 0
    right = len(mas) - 1

    while left <= right:

        m = (left + right) // 2
        if mas[m] == element:
            return m + 1
        elif element > mas[m]:
            left = m + 1
        else:
            right = m - 1

    return -1


n, *mas = [int(i) for i in input().split()]
n, *values = [int(i) for i in input().split()]
answers = [binary(mas, i) for i in values]
print(*answers)
