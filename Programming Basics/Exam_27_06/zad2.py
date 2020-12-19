intelligence = int(input())
strength = int(input())
gender = input()

bee = ''
if intelligence >= 80 and strength >= 80 and gender == "female":
    bee = "Queen Bee"
elif intelligence >= 80 and strength >= 0 and (gender == "female" or gender == "male"):
    bee ='Repairing Bee'
elif intelligence >= 60 and strength >= 0 and (gender == "female" or gender == "male"):
    bee = 'Cleaning Bee'
elif intelligence >= 0 and strength >= 80 and gender == "male":
    bee = 'Drone Bee'
elif intelligence >= 0 and strength >= 60 and (gender == "female" or gender == "male"):
    bee = 'Guard Bee'
elif intelligence >= 0 and strength >= 0 and (gender == "female" or gender == "male"):
    bee = 'Worker Bee'

print(bee)