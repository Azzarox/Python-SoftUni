VOWELS = {'a', 'o', 'u', 'e', 'i'}
# with list comprehension and .add() method
# [VOWELS.add(el.upper()) for el in list(VOWELS)]  # -> обръщаме към list(VOWELS) не можем да променяме set-а в по време на цикълът
# with set methods .union()

VOWELS = VOWELS.union(el.upper() for el in VOWELS) # with union() and generator object // if we dont reassign value it wont change

text = input()
for ch in text:
    if ch in VOWELS:
        text = text.replace(ch, "")

print(text)


# TODO: от презентацията
# write me

VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(el.upper() for el in VOWELS)

text = input()
result = [ch for ch in text if ch not in VOWELS]
print("".join(result))


# TODO: от презентацията

# text = 'ILOvePython'

VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)
# [VOWELS.add(x.upper()) for x in list(VOWELS)]

# result = []
# for ch in text:
#     if ch not in VOWELS:
#         result.append(ch)
#
# print(result)

text = input()
result = [ch for ch in text if ch not in VOWELS]
print(''.join(result))