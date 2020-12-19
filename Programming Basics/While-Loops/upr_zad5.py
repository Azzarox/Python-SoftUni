money = float(input())

x = money * 100
counter = 0

while True:
    counter += 1
    if x >= 200:
        x -= 200
    elif x >= 100:
        x -= 100
    elif x >= 50:
        x -= 50
    elif x >= 20:
        x -= 20
    elif x >= 10:
        x -= 10
    elif x >= 5:
        x -= 5
    elif x >= 2:
        x -= 2
    elif x >= 1:
        x -= 1
    if x < 1:
        break

print(counter)