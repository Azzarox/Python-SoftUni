town = input()
volume = float(input())

price = 0
percent = 0
if town == "Sofia":
    if 0 <= volume <= 500:
        percent = 0.05
        price = volume * percent
        print(f'{price:.2f}')
    elif 500 < volume <= 1000:
        percent = 0.07
        price = volume * percent
        print(f'{price:.2f}')
    elif 1000 < volume <= 10000:
        percent = 0.08
        price = volume * percent
        print(f'{price:.2f}')
    elif volume > 10000:
        percent = 0.12
        price = volume * percent
        print(f'{price:.2f}')
    else:
        print('error')

elif town == "Varna":
    if 0 <= volume <= 500:
        percent = 0.045
        price = volume * percent
        print(f'{price:.2f}')
    elif 500 < volume <= 1000:
        percent = 0.075
        price = volume * percent
        print(f'{price:.2f}')
    elif 1000 < volume <= 10000:
        percent = 0.10
        price = volume * percent
        print(f'{price:.2f}')
    elif volume > 10000:
        percent = 0.13
        price = volume * percent
        print(f'{price:.2f}')
    else:
        print('error')
elif town == "Plovdiv":
    if 0 <= volume <= 500:
        percent = 0.055
        price = volume * percent
        print(f'{price:.2f}')
    elif 500 < volume <= 1000:
        percent = 0.08
        price = volume * percent
        print(f'{price:.2f}')
    elif 1000 < volume <= 10000:
        percent = 0.12
        price = volume * percent
        print(f'{price:.2f}')
    elif volume > 10000:
        percent = 0.145
        price = volume * percent
        print(f'{price:.2f}')
    else:
        print('error')

elif (town != "Plovdiv" or town != "Sofia" or town != "Varna") or volume < 0:
    print('error')


