budget = float(input())
season = input()

type = ''
destination = ''
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type = "Camp"
        price = budget * 0.3
    else:
        type = "Hotel"
        price = budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type = "Camp"
        price = budget * 0.4
    else:
        type = "Hotel"
        price = budget * 0.8

else:
    destination = "Europe"
    type = "Hotel"
    price = budget * 0.9

print(f'Somewhere in {destination}')
print(f'{type} - {price:.2f}')
