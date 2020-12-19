def ascii_chars(chr_1, chr_2):
    # string = [ord(chr_1), ord(chr_2)]
    new_list = []
    for char in range(ord(chr_1) + 1, ord(chr_2)):
        new_list.append(chr(char))

    output = " ".join(new_list)
    return output


character_1 = input()
character_2 = input()


print(ascii_chars(character_1, character_2))
