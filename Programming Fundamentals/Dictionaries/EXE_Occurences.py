text = input()

occurences = {}

for char in text:
    if char == " ":
        continue
    if char not in occurences:
        occurences[char] = 1
    else:
        occurences[char] += 1


for key, value in occurences.items():
    print(f'{key} -> {value}')
