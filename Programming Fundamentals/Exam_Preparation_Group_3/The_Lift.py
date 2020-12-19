n_people = int(input())
lift = [int(el) for el in input().split()]
MAX_SEATS = 4

for index in range(len(lift)):
    while not lift[index] == MAX_SEATS:
        if n_people > 0:
            lift[index] += 1
            n_people -= 1
        else:
            break
max_people_lift_seats = len(lift) * MAX_SEATS
if n_people == 0 and sum(lift) < max_people_lift_seats:
    print(f'The lift has empty spots!')
elif n_people > 0 and sum(lift) == max_people_lift_seats:
    print(f"There isn't enough space! {n_people} people in a queue!")
print(' '.join(str(el) for el in lift))


# nqkvo laino

# people_waiting_for_a_lift = int(input())
# seats_available = list(map(int, input().split()))
#
# # x = people_waiting_for_a_lift // len(seats_available)
#
# is_break = False
# while people_waiting_for_a_lift > 0:
#     for i in range(len(seats_available)):
#         max_seats_available = 4
#         temp = seats_available[i]
#         if people_waiting_for_a_lift < 0:
#             is_break = True
#             break
#         if seats_available[i] < max_seats_available:
#             if people_waiting_for_a_lift < 4:
#                 seats_available[i] += people_waiting_for_a_lift
#                 people_waiting_for_a_lift -= seats_available[i]
#             else:
#                 if temp > 0 or temp != 4:
#                     seats_available[i] += max_seats_available - seats_available[i]
#                     people_waiting_for_a_lift -= seats_available[i] - temp
#
#             if sum(seats_available) - people_waiting_for_a_lift > 0:
#                 is_break = True
#                 break
#     if is_break:
#         break
#
# print(seats_available)
# print(people_waiting_for_a_lift)
#


