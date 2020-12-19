travel_fee = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
toys_count = puzzles_count+dolls_count+bears_count+minions_count+trucks_count

puzzles_count_price = puzzles_count * 2.60
dolls_count_price = dolls_count * 3
bears_count_price = bears_count * 4.10
minions_count_price = minions_count * 8.20
trucks_count_price = trucks_count * 2
toys_price = puzzles_count_price + dolls_count_price + bears_count_price + minions_count_price + trucks_count_price

if toys_count >= 50:
         discount = 0.25 * toys_price
         toys_price -= discount
         rent = toys_price * 0.1
         profit = toys_price - rent
         left_sum = profit - travel_fee
         #print(f'Yes! {abs(left_sum):.2f} lv left.')
elif toys_count < 50:
        rent = toys_price * 0.1
        profit = toys_price - rent
        left_sum = profit - travel_fee
        #print(f'Not enough money! {abs(travel_fee-profit):.2f} lv needed.')

if profit >= travel_fee:
    print(f'Yes! {abs(profit-travel_fee):.2f} lv left.')
elif profit < travel_fee:
    print(f'Not enough money! {abs(travel_fee - profit):.2f} lv needed.')

# summary
# if the profit is less than the travel fee it can go to negative number so w euse abs()
# profit can be equal to the travel price and it should get a 0lv left:
#
#
