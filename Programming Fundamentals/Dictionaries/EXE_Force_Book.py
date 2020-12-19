data = input()

force_book = {}

while not data == "Lumpawaroo":
    delimiter = data.split()
    if "|" in data:
        force_side, force_user = data.split(" | ")
        if force_side not in force_book:
            force_book[force_side] = []

        all_values = []

        for current_list in force_book.values():
            all_values += current_list

        if force_user not in all_values:
            force_book[force_side].append(force_user)
    else:
        force_user, force_side = data.split(" -> ")
        old_side = ""
        for key, value in force_book.items():
            if force_user in value:
                old_side = key
                break
        if old_side != "":
            force_book[old_side].remove(force_user)

            if force_side not in force_book:
                force_book[force_side] = []

            force_book[force_side].append(force_user)
        else:
            if force_side not in force_book:
                force_book[force_side] = []

            if force_user not in force_book[force_side]:
                force_book[force_side].append(force_user)

        print(f'{force_user} joins the {force_side} side!')

    data = input()

order = sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0]))

for key, value in order:
    if len(value) == 0:
        continue
    print(f'Side: {key}, Members: {len(value)}')
    for user in sorted(value):
        print(f'! {user}')