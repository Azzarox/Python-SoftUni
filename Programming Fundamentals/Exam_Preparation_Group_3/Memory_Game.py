def play_round(cards, i_1, i_2, round_num):
    if i_1 == i_2 or i_1 not in range(len(cards)) or i_2 not in range(len(cards)):
        print("Invalid input! Adding additional elements to the board")
        card = f"-{round_num}a"
        middle = len(cards) // 2
        cards.insert(middle, card)
        cards.insert(middle + 1, card)
        return cards

    if cards[i_1] == cards[i_2]:
        element = cards[i_1]
        print(f"Congrats! You have found matching elements - {element}!")
        cards.remove(element)
        cards.remove(element)
        return cards
    print("Try again!")
    return cards


memory_cards = input().split()
command = input()

counter = 0

while not command == 'end':
    index_1, index_2 = [int(el) for el in command.split()]
    counter += 1
    memory_cards = play_round(memory_cards, index_1, index_2, counter)
    if len(memory_cards) == 0:
        print(f"You have won in {counter} turns!")
        exit(0)
    command = input()

print("Sorry you lose :(")
print(' '.join(memory_cards))

### 66/100

# sequence = input().split()
#
# line = input()
# moves_count = 0
# first_index_add = len(sequence) // 2
#
# while line != "end":
#
#     index_1 = int(line.split()[0])
#     index_2 = int(line.split()[1])
#     moves_count += 1
#     if index_1 == index_2 or index_1 not in range(len(sequence)) or index_2 not in range(len(sequence)):
#         # "-{number of moves until now}a
#         sequence.insert(first_index_add - 1, f'-{moves_count}a')
#         sequence.insert(first_index_add, f'-{moves_count}a')
#         print(f'Invalid input! Adding additional elements to the board')
#     if sequence[index_1] == sequence[index_2]:
#         print(f"Congrats! You have found matching elements - {sequence[index_1]}!")
#         temp = sequence
#         card = sequence[index_1]
#         sequence.remove(card)
#         sequence.remove(card)
#     elif sequence[index_1] != sequence[index_2] and index_1 != -1 and index_2 != -1:
#         print('Try again!')
#
#     if not sequence:
#         print(f"You have won in {moves_count} turns!")
#         exit(0)
#
#     line = input()
#
# print('Sorry you lose :(')
# print(' '.join(sequence))
