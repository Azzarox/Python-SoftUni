class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


me = Person('John', "Vasilev", "25")
print(me.first_name)
print(me.second_name)
print(me.age)