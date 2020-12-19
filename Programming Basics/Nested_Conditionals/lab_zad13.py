#room for one person = 18lv za noshtuvka
#apartment = 25lv za noshtuvka
#president apartment = 25lv za noshtuvka

#prestoi = 11dni - 1 == 10 noshtuvki

x = int(input())
house_type = input()
grade = input()

days = x - 1


if house_type == "apartment":
    total_price = days * 25
    if days < 10:

        total_price -= total_price * 0.3
    elif days < 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5

elif house_type == "president apartment":
    total_price = days * 35
    if days < 10:
        total_price -= total_price * 0.1
    elif days < 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.2

elif house_type == "room for one person":
    total_price = days * 18

if grade == "positive":
    total_price += total_price * 0.25
elif grade == "negative":
    total_price -= total_price * 0.10

print(f'{total_price:.2f}')