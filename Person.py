# Примитивное описание человека
class Person():
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def get_weight(self):
        weight = self.height - 100
        print(f'The person weight is {weight} kg')

student_person = Person(25, 184)
student_person.get_weight()