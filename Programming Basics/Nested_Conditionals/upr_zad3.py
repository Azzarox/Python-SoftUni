flowers = input()
count = int(input())
budget = int(input())

price = 0
if flowers == "Roses":
    price = count * 5
    if count > 80:
        price -= price * 0.1
elif flowers == "Dahlias":
    price = count * 3.80
    if count > 90:
        price -= price * 0.15
elif flowers == "Tulips":
    price = count * 2.80
    if count > 80:
        price -= price * 0.15
elif flowers == "Narcissus":
    price = count * 3
    if count < 120:
        price += price * 0.15
else:
    price = count * 2.50
    if count < 80:
        price += price * 0.2

diff = abs(budget - price)

if budget >= price:
    print(f'Hey, you have a great garden with {count} {flowers} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')