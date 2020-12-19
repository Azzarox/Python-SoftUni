journal = input().split(", ")

input_command = input()

while input_command != "Craft!":

    args = input_command.split(" - ")

    command = args[0]
    item = args[1]

    if command == "Collect":
        # if item in journal:
        #     input_command = input()
        #     continue
        #
        # journal.append(item)
        if item not in journal:
            journal.append(item)
    elif command == "Drop":
        # if item not in journal:
        #     input_command = input()
        #     continue
        #
        # journal.remove(item)
        if item in journal:
            journal.remove(item)
    elif command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in journal:
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index+1, new_item)
    elif command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)
    input_command = input()

print(", ".join(journal))
