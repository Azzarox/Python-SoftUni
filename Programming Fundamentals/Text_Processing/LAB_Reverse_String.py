line = input()
while line != "end":
    word = line[::-1]
    print(f'{line} = {word}')
    line = input()
