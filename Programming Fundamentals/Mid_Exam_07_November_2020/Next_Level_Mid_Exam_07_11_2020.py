experience = float(input())
battles_count = int(input())

total_experience = 0
count = 0
for battle in range(1, battles_count + 1):
    count += 1
    exp_per_battle = float(input())
    if battle % 3 == 0:
        exp_per_battle += exp_per_battle * 0.15
    if battle % 5 == 0:
        exp_per_battle -= exp_per_battle * 0.1
    if battle % 15 == 0:
        exp_per_battle += exp_per_battle * 0.05
    total_experience += exp_per_battle
    if total_experience >= experience:
        break

if total_experience >= experience:
    print(f'Player successfully collected his needed experience for {count} battles.')
else:
    print(f'Player was not able to collect the needed experience, {experience - total_experience:.2f} more needed.')
