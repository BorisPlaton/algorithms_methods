backpack = [int(i) for i in input().split()]
items = [[int(i) for i in input().split()] for i in range(backpack[0])]
items.sort(key=lambda x: x[0] / x[1], reverse=True)
cost = 0

for item in items:
    if backpack[1]:
        if item[1] <= backpack[1]:
            cost += item[0]
            backpack[1] -= item[1]
        else:
            cost += item[0] * backpack[1] / item[1]
            break
    else:
        break

print(f"{cost:.3f}")
