money = float(input())
saved_money = float(input())

days = 0
spend_count = 0

while True:
    command = input()
    days += 1
    amount = float(input())

    if command == "spend":
        if amount > saved_money:   #iskam da poharcha 200 no imam 100
            amount = saved_money    # sledovatelno 200 stava 100
        saved_money -= amount       # 100 - 100 = 0
        spend_count += 1

        if spend_count == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break
    else:
        saved_money += amount
        spend_count = 0

    if saved_money >= money:
        print(f'You saved the money for {days} days.')
        break

