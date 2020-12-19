days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_price = 45
waffles_price = 5.80
pancake_price = 3.20

money_per_day = ((cakes_count * cakes_price) + (waffles_price * waffles_count) + (pancakes_count * pancake_price)) * bakers_count

income = money_per_day * days_count
profit = income - (income / 8)
print(profit)