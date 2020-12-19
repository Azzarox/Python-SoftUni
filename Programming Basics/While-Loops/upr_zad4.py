target = 10000

total = 0
while total < target:       #while with condition:
    line = input()

    if line == "Going home":
        steps_to_home = int(input())
        total += steps_to_home
        break

    steps = int(line)
    total += steps

if total < target:
    print(f'{target - total} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{abs(total - target)} steps over the goal!')





