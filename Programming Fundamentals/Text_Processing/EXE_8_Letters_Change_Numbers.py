
def position_letter(letter):
    position = ord(letter) - 64

    if letter.islower():
        position = ord(letter) - 96

    return position


def calculate_item_result(item):
    first_letter = item[0]
    last_letter = item[-1]
    number = int(item[1:-1])
    first_letter_position = position_letter(first_letter)
    last_letter_position = position_letter(last_letter)

    res = 0

    if first_letter.isupper():
        res = number / first_letter_position
    else:
        res = number * first_letter_position

    if last_letter.isupper():
        res -= last_letter_position
    else:
        res += last_letter_position

    return res


items = input().split()

total_sum = 0
for item in items:
    res = calculate_item_result(item)
    total_sum += res

print(f'{total_sum:.2f}')
