groceries_list = input().split("!")

command = input()
while command != "Go Shopping!":
    command_type, item = command.split(" ", 1)

    if command_type == "Urgent":
        if item not in groceries_list:
            groceries_list.insert(0, item)
    elif command_type == "Unnecessary":
        if item in groceries_list:
            groceries_list.remove(item)
    elif command_type == "Correct":
        old_item, new_item = item.split()
        if old_item in groceries_list:
            old_item_index = groceries_list.index(old_item)
            groceries_list[old_item_index] = new_item
    elif command_type == "Rearrange":
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)
    command = input()

print(', '.join(groceries_list))
