data = input()

users = {}
while not data == "Log out":

    commands_data = data.split(": ")
    command = commands_data[0]
    if command == "New follower":
        user = commands_data[1]
        if user in users:
            data = input()
            continue
        elif user not in users:
            users[user] = {"comments": 0, "likes": 0}
    elif command == "Like":
        user = commands_data[1]
        likes = int(commands_data[2])
        if user in users:
            users[user]['likes'] += likes
        elif user not in users:
            users[user] = {"comments": 0, "likes": 0}
            users[user]['likes'] = likes
    elif command == "Comment":
        user = commands_data[1]
        if user not in users:
            users[user] = {"comments": 1, "likes": 0}
        elif user in users:
            users[user]["comments"] += 1
    elif command == "Blocked":
        user = commands_data[1]
        if user not in users:
            print(f"{user} doesn't exist.")
        elif user in users:
            del users[user]

    data = input()

print(f"{len(users)} followers")
store_sum = {}
for key, value in users.items():
    store_sum[key] = value["comments"] + value["likes"]

sorted_store_sum = sorted(store_sum.items(), key=lambda x: (-x[1], x[0]))

for name, value in sorted_store_sum:
    print(f'{name}: {value}')
