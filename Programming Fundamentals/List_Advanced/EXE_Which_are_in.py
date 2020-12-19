my_items = input().split(", ")
other_items = input()

checker_items = [item for item in my_items if item in other_items]

print(checker_items)

# to_check !!!
