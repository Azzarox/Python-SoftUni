day = input()

is_weekend = day == "Saturday" or day == "Sunday"

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif is_weekend:
    print("Weekend")
else:
    print("Error")