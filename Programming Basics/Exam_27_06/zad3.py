flower_type = input()
count_flower = int(input())
season = input()

honey = 0
if season == "Spring":
    if flower_type == "Sunflower":
        honey = 10
    elif flower_type == "Daisy":
        honey = 12
    elif flower_type == "Lavender":
        honey = 12
    elif flower_type == "Mint":
        honey = 10
elif season == "Summer":
    if flower_type == "Sunflower":
        honey = 8
    elif flower_type == "Daisy":
        honey = 8
    elif flower_type == "Lavender":
        honey = 8
    elif flower_type == "Mint":
        honey = 12
elif season == "Autumn":
    if flower_type == "Sunflower":
        honey = 12
    elif flower_type == "Daisy":
        honey = 6
    elif flower_type == "Lavender":
        honey = 6
    elif flower_type == "Mint":
        honey = 6

production = count_flower * honey

if season == "Summer":
    production += production * 0.1
elif season == "Autumn":
    production -= production * 0.05
elif season == "Spring":
    if flower_type == "Mint" or flower_type == "Daisy":
        production += production * 0.1

print(f'Total honey harvested: {production:.2f}')