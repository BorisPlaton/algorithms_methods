def merge(mas1, mas2):
    res = []
    i1 = 0
    i2 = 0
    inv = 0
    while i1 < len(mas1) and i2 < len(mas2):
        if mas1[i1] > mas2[i2]:
            inv += len(mas1) - i1
            res.append(mas2[i2])
            i2 += 1
        elif mas1[i1] == mas2[i2]:
            try:
                inv += len(mas1) - i1 - 1
            except IndexError:
                pass
            res.append(mas2[i2])
            res.append(mas1[i1])
            i1 += 1
            i2 += 1
        else:
            res.append(mas1[i1])
            i1 += 1

    if i1 < len(mas1):
        return res + mas1[i1:], inv
    else:
        return res + mas2[i2:], inv


def merge_sort(mas):
    if len(mas) == 1:
        return mas, 0
    m = len(mas) // 2
    left, inv1 = merge_sort(mas[:m])
    right, inv2 = merge_sort(mas[m:])
    mg = merge(left, right)
    return mg[0], mg[1] + inv1 + inv2


input()
print(merge_sort([int(i) for i in input().split()])[1])
