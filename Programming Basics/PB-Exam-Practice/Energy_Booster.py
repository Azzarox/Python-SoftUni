#total = ?

fruit = input()
name_of_set = input()
count = int(input())

price = 0
if name_of_set == "small":
    if fruit == "Watermelon":
        price = 2*56
    elif fruit == "Mango":
        price = 2*36.66
    elif fruit == "Pineapple":
        price = 2*42.10
    elif fruit == "Raspberry":
        price = 2*20
else:
    if fruit == "Watermelon":
        price = 5*28.70
    elif fruit == "Mango":
        price = 5*19.60
    elif fruit == "Pineapple":
        price = 5*24.80
    elif fruit == "Raspberry":
        price = 5*15.20

total = count * price

if 400 <= total <= 1000:
    total -= total*0.15
elif total > 1000:
    total -= total *0.5

print(f'{total:.2f} lv.')