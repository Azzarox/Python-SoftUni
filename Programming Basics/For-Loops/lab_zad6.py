text = input()

character_sum = 0
for character in text:
    if character == "a":
        character_sum += 1
    elif character == "e":
        character_sum += 2
    elif character == "i":
        character_sum += 3
    elif character == "o":
        character_sum += 4
    elif character == "u":
        character_sum += 5

print(character_sum)