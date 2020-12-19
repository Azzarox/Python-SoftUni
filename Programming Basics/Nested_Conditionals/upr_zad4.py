budget = int(input())
season = input()
fishermen_count = int(input())

price = 0
if season == "Spring":
    price = 3000
    if fishermen_count <= 6:
        price -= price * 0.10
    elif fishermen_count <= 11:
        price -= price * 0.15
    else:
        price -= price * 0.25

elif season == "Winter":
    price = 2600
    if fishermen_count <= 6:
        price -= price * 0.10
    elif fishermen_count <= 11:
        price -= price * 0.15
    else:
        price -= price * 0.25

elif season == "Autumn" or season == "Summer":
    price = 4200
    if fishermen_count <= 6:
        price -= price * 0.10
    elif fishermen_count <= 11:
        price -= price * 0.15
    else:
        price -= price * 0.25

if fishermen_count % 2 == 0 and season != "Autumn":
    price -= price * 0.05

diff = abs(budget - price)
if budget >= price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')