class Party:
    def __init__(self):
        self.people = []


party = Party()

command = input()
counter = 0
while command != 'End':
    counter += 1

    party.people.append(command)

    command = input()

print(f'Going: {", ".join(party.people)}')
print(f'Total: {counter}')
