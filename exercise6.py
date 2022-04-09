number = int(input())

if number == 1:
    print(1, number, sep="\n")
elif number == 2:
    print(1, number, sep="\n")
else:
    answers = []
    s = 0
    for num in range(1, number):
        if num < number - s:
            answers.append(num)
            s += num
        elif num == number - s:
            answers.append(num)
            print(len(answers))
            print(*answers, sep="\n")
            break
        else:
            answers.append(number - (s - answers.pop()))
            print(len(answers))
            print(*answers, sep="\n")
            break

