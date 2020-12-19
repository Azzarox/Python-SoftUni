# med = int(input())
# line = False
#
# total_sum = 0
# while True:
#     name = input()
#     if name == "Winter has come":
#         if total > med:
#             print(f'Well done! Honey surplus {total - med}.')
#         else:
#             print(f'Hard Winter! Honey needed {med - total}.')
#         break
#     total = 0
#     for i in range(6):
#         if total < 0:
#             print(f'{name} was banished for gluttony')
#         name = float(input())
#         total += name
#         total_sum += name
#         if name == "Winter has come":
#             break

# ne raboti pravilno posledniqt primer ot zadachata v word-document-a

honey_needed = float(input())
total = 0

while True:
    name_of_the_bee = input()
    if name_of_the_bee != 'Winter has come':
        for i in range(6):
            monthly_honey_carried_by_the_bee = float(input())
            harvested_per_month_into_string = str(monthly_honey_carried_by_the_bee)
            if harvested_per_month_into_string == 'Winter has come':
                if total >= honey_needed:
                    print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
                    break
                elif total < honey_needed:
                    print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
                    break
            total += monthly_honey_carried_by_the_bee
        if total < 0:
            print(f'{name_of_the_bee} was banished for gluttony')
        if total >= honey_needed:
            print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
            break
    elif name_of_the_bee == 'Winter has come':
        if total >= honey_needed:
            print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
            break
        elif total < honey_needed:
            print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
            break

# bez flag-promenliva



# s flag-promenliva -> (koqto e useless , zashtoto se prekusva samo ediniqt cikul a ne i dvata da spirat kogato ediniqt spira)

# honey_needed = float(input())
# total = 0
# flag = False
#
# while True:
#     name_of_the_bee = input()
#     if name_of_the_bee != 'Winter has come':
#         for i in range(6):
#             monthly_honey_carried_by_the_bee = float(input())
#             harvested_per_month_into_string = str(monthly_honey_carried_by_the_bee)
#             if harvested_per_month_into_string == 'Winter has come':
#                 if total >= honey_needed:
#                     print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
#                     flag = True
#                     break
#                 elif total < honey_needed:
#                     print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
#                     flag = True
#                     break
#             total += monthly_honey_carried_by_the_bee
#         if total < 0:
#             print(f'{name_of_the_bee} was banished for gluttony')
#         if total >= honey_needed:
#             print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
#             flag = True
#             break
#     elif name_of_the_bee == 'Winter has come':
#         if total >= honey_needed:
#             print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
#             flag = True
#             break
#         elif total < honey_needed:
#             print(f'Hard Winter! Honey needed {(honey_needed - total):.2f}.')
#             flag = True
#             break
#     if flag:
#         break



