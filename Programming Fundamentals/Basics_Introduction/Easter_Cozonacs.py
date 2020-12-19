budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4  # *1.25 zashtoto e za 1Litur mlqko i /4 zashtoto e 1000/4 = 250ml

cozonac_price = eggs_price + flour_price + milk_price

cozonac_counter = 0
colored_eggs = 0
while budget >= cozonac_price:
    cozonac_counter += 1
    colored_eggs += 3
    if cozonac_counter % 3 == 0:
        colored_eggs -= cozonac_counter - 2
    budget -= cozonac_price

print(f'You made {cozonac_counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')