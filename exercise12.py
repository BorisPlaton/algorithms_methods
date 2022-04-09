import bisect


def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    mid = len(mas) // 2
    left = [i for i in mas if i < mas[mid]]
    middle = [i for i in mas if i == mas[mid]]
    right = [i for i in mas if i > mas[mid]]
    return quick_sort(left) + middle + quick_sort(right)


n, m = [int(i) for i in input().split()]
start = []
end = []

for i in range(n):
    line = [int(i) for i in input().split()]
    start.append(line[0])
    end.append(line[1])

points = [int(i) for i in input().split()]
res = []

start = quick_sort(start)
end = quick_sort(end)

for point in points:
    res.append(bisect.bisect_right(start, point) - bisect.bisect_left(end, point))

print(*res)
