from collections import deque


n = int(input())
stations = deque()

for _ in range(n):
    stations.append(input())

for big_circle in range(n): # от коя станция започваме
    is_valid = True
    tank_petrol = 0 # всеки път ще се занулява, ако не е валидно

    for small_circle in range(n):  # въртим през станциите
        current_station = stations[small_circle]

        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        tank_petrol += petrol - distance_to_next_station

        if tank_petrol < 0: # ако е отрицателно значи че няма да можем да стигнем до следващата бензиностанция и е невалидно
            stations.append(stations.popleft())
            is_valid = False # ако не можем да стигнем излизаме и отиваме да увеличим стартовата ни позиция (big circle)
            break

    if is_valid:
        print(big_circle)
        break
