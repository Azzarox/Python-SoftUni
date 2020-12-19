class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animals(self, species, name):

        if species == "mammal":
            self.mammals.append(name)
        elif species == "birds":
            self.birds.append(name)
        elif species == "fish":
            self.fish.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        result = ''
        if species == "mammal":
            result += f'Mammals in {self.name}: {", ".join(self.mammals)}\n'
        elif species == "fish":
            result += f'Fishes in {self.name}: {", ".join(self.fish)}\n'
        else:
            result += f'Birds in {self.name}: {", ".join(self.birds)}\n'
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)

count = int(input())

for animal in range(count):
    specie, name = input().split()
    zoo.add_animals(specie, name)

info = input()
print(zoo.get_info(info))
