walk_minutes = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

total_minutes = walk_minutes * walks_per_day
calories_burned = total_minutes*5
half_taken_calories = calories_per_day / 2

if calories_burned >= half_taken_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.')