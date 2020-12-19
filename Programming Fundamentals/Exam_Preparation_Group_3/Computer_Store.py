total = 0
total_price_without_taxes = 0
total_taxes = 0
is_valid = True
while True:
    prices_without_tax = input()
    if prices_without_tax == "special" or prices_without_tax == "regular":
        break
    float_prices_without_tax = float(prices_without_tax)
    if float_prices_without_tax > 0:
        total_price_without_taxes += float_prices_without_tax
        taxes = float_prices_without_tax * 0.2
        total_taxes += taxes
        tax_price = float_prices_without_tax + float_prices_without_tax * 0.2
        total += tax_price
    elif float_prices_without_tax < 0:
        print('Invalid price!')
        continue

if prices_without_tax == "special":
    total -= total * 0.1

if total <= 0:
    is_valid = False
    print('Invalid order!')

if is_valid:
    print(f'''Congratulations you've just bought a new computer!
Price without taxes: {total_price_without_taxes:.2f}$
Taxes: {total_taxes:.2f}$
-----------
Total price: {total:.2f}$
''')
