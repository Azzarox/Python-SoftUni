n = int(input())

catalog = {}

for _ in range(n):
    data = input().split()
    command = data[0]
    name = data[1]

    if command == "register":
        if name in catalog:
            print(f'ERROR: already registered with plate number {catalog[name]}')
        else:
            plate = data[2]
            catalog[name] = plate
            print(f'{name} registered {plate} successfully')

    if command == "unregister":
        if name not in catalog:
            print(f'ERROR: user {name} not found ')
        else:
            catalog.pop(name)
            print(f'{name} unregistered successfully')

for key, value in catalog.items():
    print(f'{key} => {value}')
