# Without watching anything - completely solo - awesome - 100/100 - dictionary

n = int(input())

cars = {}

for _ in range(n):
    cars_data = input().split("|")
    car = cars_data[0]
    mileage = int(cars_data[1])
    fuel = int(cars_data[2])
    cars[car] = {"mileage":mileage, "fuel": fuel}

data = input()

while not data == "Stop":
    commands_data = data.split(" : ")
    command = commands_data[0]
    if command == "Drive":
        car = commands_data[1]
        distance = int(commands_data[2])
        fuel = int(commands_data[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        elif cars[car]["fuel"] >= fuel:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
        if cars[car]["mileage"] >= 100000:
            print(f'Time to sell the {car}!')
            del cars[car]
    elif command == "Refuel":
        car = commands_data[1]
        fuel = int(commands_data[2])
        if cars[car]["fuel"] + fuel >= 75:
            print(f'{car} refueled with {75 - cars[car]["fuel"]} liters')
            cars[car]["fuel"] = 75
        else:
            cars[car]["fuel"] += fuel
            print(f'{car} refueled with {fuel} liters')
    elif command == "Revert":
        car = commands_data[1]
        kilometers = int(commands_data[2])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"] < 10000:
            cars[car]["mileage"] = 10000
            data = input()
            continue
        print(f'{car} mileage decreased by {kilometers} kilometers')
    data = input()


sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]["mileage"], x[0]))

for car, value in sorted_cars:
    print(f'{car} -> Mileage: {value["mileage"]} kms, Fuel in the tank: {value["fuel"]} lt.')

