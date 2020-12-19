while True:
    line = input()
    if line == "End":
        break
    destination = line
    budget = float(input())
    saved_money = 0
    while saved_money < budget:
        current_saved = float(input())
        saved_money += current_saved
    print(f'Going to {destination}!')

# line = None
# while line != "End":
#     line = input()
#     destination = line
#     budget = float(input())
#     saved_money = 0
#     while saved_money < budget:
#         money = float(input())
#         saved_money += money
#     print(f'Going to {destination}!')
# not working~!
