from collections import deque
from datetime import datetime, timedelta

data = input().split(";")
time = datetime.strptime(input(),"%H:%M:%S")  # -> datetime - library/ caps H S M -> with leading zero 01 02 and not 1 2

robots = []

available_robots = []

for el in data:  # напълва списък с dictionary от роботите и тяхното име, време, и кога ще е свободен
    robot_data = el.split("-")
    # robot = {"name": robot_data[0], "processing_time": int(robot_data[1]), "available_at": time} -> като долното но съкратен запис
    robot = {}
    robot["name"] = robot_data[0]
    robot["processing_time"] = int(robot_data[1])
    robot["available_at"] = time
    robots.append(robot)
    available_robots.append(robot)

available_robots = deque(available_robots)

product = input()
products = []
while product != "End":  # напълва списък с продуктите
    products.append(product)
    product = input()

products = deque(products)

time = time + timedelta(seconds=1)  # започва работата по продуктите

while len(products) > 0:
    current_product = products.popleft()  # взима продукта

    if available_robots:
        current_robot = available_robots.popleft()  # поп-ва dictionary от 1вия робот
        current_robot["available_at"] = time + timedelta(seconds=current_robot["processing_time"])  # след като го е попнало, изчислява кога щее готов
        robot = [el for el in robots if el == current_robot][0]  # вади дикт-а със първия робот (current_robot)
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots: # r са роботите един по един в robots
            if time >= r["available_at"]: # проверява дали е изминало достатъчно време до тогава когато трябва да е свободен
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()  # същият код като от 38 линия
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            print(f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")

    time = time + timedelta(seconds=1)