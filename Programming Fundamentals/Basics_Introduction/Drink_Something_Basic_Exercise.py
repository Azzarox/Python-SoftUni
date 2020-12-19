age = int(input())

kind = ''
drink = ''
if age <= 14:
    kind = 'Kids'
    drink = 'toddy'
elif age <= 18:
    kind = 'Teens'
    drink = 'coke'
elif age <= 21:
    kind = 'Young adults'
    drink = 'beer'
elif age > 21:
    kind = 'Adults'
    drink = 'whisky'

print(f'drink {drink}')

