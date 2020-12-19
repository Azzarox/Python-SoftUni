record = float(input())
distance = float(input())
time_per_meter = float(input())

time = time_per_meter * distance
slow = (distance // 50) * 30

total = time + slow
if total >= record:
    print(f'No! He was {total-record:.2f} seconds slower.')
else:
    print(f'Yes! The new record is {total:.2f} seconds.')

