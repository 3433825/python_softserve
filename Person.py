class Person():
    def __init__(self, age, height):
        self.age = age
        self.height = height

    def get_weight(self):
        weight = self.height - 100
        return weight

class Student(Person):
    """ docs """
    def __init__(self, age, height, group):
        super().__init__(age, height)
        self.group = group

    def get_weight(self):
        person_weight = super().get_weight()
        student_weight = person_weight - 10
        return student_weight

class Teacher(Person):
    def __init__(self, age, height, experience):
        super().__init__(age, height)
        self.experience = experience

    def get_weight(self):
        person_weight = super().get_weight()
        teacher_weight = person_weight + 10
        return teacher_weight

person = Person(35, 186)
student = Student(20, 185, "A")
teacher = Teacher(42, 178, 10)

print(f'The person weight is {person.get_weight()} kg')
print(f'The student weight is {student.get_weight()} kg')
print(f'The teacher weight is {teacher.get_weight()} kg')
