# same but with functions


def add(name, items, available):
    if name not in available:
        return print('Card not found.')
    items.append(name)
    return items


def insert(name, items, ava_cards):
    name_of_card, card_index = name.split()
    card_index = int(card_index)
    if card_index not in range(-(len(ava_cards)), len(ava_cards)) or name_of_card not in ava_cards:
        return print('Error!')
    return items.insert(card_index, name_of_card)


def remove(name, items):
    if name in items:
        return items.remove(name)
    return print("Card not found.")


def swap(name, items):
    tokens = name.split()
    card_1 = tokens[0]
    card_2 = tokens[1]
    index_1 = int(items.index(card_1))
    index_2 = int(items.index(card_2))
    items[index_1], items[index_2] = items[index_2], items[index_1]


def shuffle(items):
    items = items[::-1]
    return items


cards = input().split(":")

line = input()
deck = []
while line != "Ready":
    command, card_name = line.split(" ", 1)
    if command == "Add":
        add(card_name, deck, cards)
    if command == "Insert":
        insert(card_name, deck, cards)
    if command == "Remove":
        remove(card_name, deck)
    if command == "Swap":
        swap(card_name, deck)
    if command == "Shuffle":
        deck = shuffle(deck)

    line = input()

print(" ".join(deck))

# # 90pts

# cards = input().split(":")
#
# line = input()
# deck = []
# while line != "Ready":
#     command, card_name = line.split(" ", 1)
#
#     if command == "Add":
#         if card_name not in cards:
#             print('Card not found.')
#         else:
#             deck.append(card_name)
#     if command == "Insert":
#         card_name, card_index = card_name.split()
#         card_index = int(card_index)
#         if card_index not in range(-(len(cards)), len(cards)) or card_name not in cards:
#             print('Error!')
#         else:
#             deck.insert(card_index, card_name)
#     if command == "Remove":
#         if card_name not in deck:
#             print('Card not found.')
#         else:
#             deck.remove(card_name)
#
#     if command == "Swap":
#         card_name_1 = card_name.split()[0]
#         card_name_2 = card_name.split()[1]
#         card_name_index_1 = int(deck.index(card_name_1))
#         card_name_index_2 = int(deck.index(card_name_2))
#         deck[card_name_index_1], deck[card_name_index_2] = deck[card_name_index_2], deck[card_name_index_1]
#         # deck[int(card_name_index_1)], deck[int(card_name_index_2)] = deck[int(card_name_index_2)], deck[
#         #     int(card_name_index_1)]
#
#     if command == "Shuffle":
#         deck = deck[::-1]
#
#     line = input()
#
# print(" ".join(deck))

