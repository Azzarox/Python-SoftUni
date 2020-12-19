account = 0

while True:
    line = input()
    if line == "NoMoreMoney":
        break
    money = float(line)             #trqbva da e float ot string-a , a ne nov input
    if money < 0:
        print(f'Invalid operation!')
        break
    account += money
    print(f'Increase: {money:.2f}')

print(f'Total: {account:.2f}')