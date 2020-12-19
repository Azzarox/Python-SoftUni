
cards = input().split(' ')
num_of_faro_shuffles = int(input())

top_card = cards[0]
bot_card = cards[-1]

half = len(cards) // 2

faro = []
for num in range(num_of_faro_shuffles):
    left_cards = []
    right_cards = []

    for index in range(1, half):
        left_cards.append(cards[index])

    for index in range(half, len(cards) - 1):
        right_cards.append(cards[index])

    for index in range(len(left_cards)):  # slaga po 2 karti na vednyj/// zavurta 3puti zaradi len = 3 v tozi sluchai
        faro.append(right_cards[index])
        faro.append(left_cards[index])

    cards = faro.copy()
    cards.append(bot_card)
    cards.insert(0, top_card)
    faro = []

print(cards)
