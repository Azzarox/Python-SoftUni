# written by me

def input_to_set(count):
    all_guests = set()
    for _ in range(count):
        all_guests.add(input())
    return all_guests


def came_people(command):
    people_came = set()
    while True:
        line = input()
        if line == command:
            break
        people_came.add(line)

    return people_came


def difference():
    return all_people_guests - people_who_came


def is_vip(person):
    return person[0].isdigit()


def separate_vip_regular(guests):
    vip_guests = []
    reg_guests = []
    for person in guests:
        if is_vip(person):
            vip_guests.append(person)
        else:
            reg_guests.append(person)
    return sorted(vip_guests), sorted(reg_guests)


def print_result(guests):
    print(len(people_who_not_come))
    (vip_guests, reg_guests) = separate_vip_regular(guests)
    for person in vip_guests:
        print(person)
    for person in reg_guests:
        print(person)


n = int(input())

all_people_guests = input_to_set(n)
people_who_came = came_people("END")
people_who_not_come = difference()

print_result(people_who_not_come)
