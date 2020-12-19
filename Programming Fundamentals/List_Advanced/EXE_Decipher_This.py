def first_letter_ascii(word):
    digits = ''
    for ch in word:
        if not ch.isdigit():
            break

        digits += ch

    ascii_value = int(digits)
    char_value = chr(ascii_value)
    new_word = word.replace(digits, char_value)
    return new_word


def switch_letter(word):
    new_word = list(word)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]

    return "".join(new_word)


def decrypt(word):
    res = first_letter_ascii(word)
    res = switch_letter(res)
    return res


words = input().split()
new_words = [decrypt(word) for word in words]
print(" ".join(new_words))

# to_check
