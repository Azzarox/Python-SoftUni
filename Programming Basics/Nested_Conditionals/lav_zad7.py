hour = int(input())
day = input()

# if 10 <= hour <= 18 and day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursaday" or day == "Friday" or day == "Saturday":
#     print('open')
# else:
#     print("closed")

if hour not in range(10,19) or day =="Sunday":
    print("closed")
else:
    print("open")