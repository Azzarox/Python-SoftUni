age = int(input())
price_wash = float(input())
toy_price = int(input())

toys = 0

money = 0
bro_take = 0
for i in range(1 , age + 1):
    if i % 2 == 0:

        money += (i*10) / 2      # 2ri roj. den = 2*10 = 20 i tva 20/2 = 10
        bro_take += 1
    else:
        toys += 1

toys_total = toys * toy_price
money_total = (money - bro_take) + toys_total

if money_total >= price_wash:
    print(f'Yes! {money_total - price_wash:.2f}')
else:
    print(f'No! {abs(money_total - price_wash):.2f}')