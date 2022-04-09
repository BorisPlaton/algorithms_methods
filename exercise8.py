code = {}
for i in range(int(input().split()[0])):
    char = [i for i in input().split(": ")]
    code[char[1]] = char[0]

current_code = ""
word = ""
for i in input():
    current_code += i
    char = code.get(current_code)
    if char:
        word += char
        current_code = ""
print(word)