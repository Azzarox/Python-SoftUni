budget = float(input())
extras = int(input())
price_per_extra = float(input())

decor = budget * 0.1
clothing = extras * price_per_extra

if extras > 150:
    clothing = clothing - (clothing * 0.1)

sum = decor + clothing

if sum <= budget:
    print(f'Action!')
    print(f'Wingard starts filming with {abs(sum-budget):.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {abs(sum - budget):.2f} leva more.')
