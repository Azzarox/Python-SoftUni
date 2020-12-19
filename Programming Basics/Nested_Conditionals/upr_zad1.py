type_cin = input()
rows = int(input())
columns = int(input())

ticket_price = 0
if type_cin == "Premiere":
    ticket_price = 12
elif type_cin == "Normal":
    ticket_price = 7.5
else:
    ticket_price = 5

leva = ticket_price * rows * columns
print(f'{leva:.2f} leva')