string_data = input()

for el in string_data:
    el = ord(el) + 3
    character = chr(el)
    print(character, end="")