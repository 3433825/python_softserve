"""
В Python, чтобы случайно выбрать элемент из списка, вы можете использовать модуль random.
"""
import random
from Data import data
from string import punctuation

exercise_list = data.SENTENCE.split(' ')
exercise_list = [x.strip(punctuation) for x in exercise_list]
print(exercise_list)

# Случайный выбор элемента из списка
random_element = random.choice(exercise_list)
print(random_element)

# Случайный выбор 3-х элементов из списка без повторений
random_elements = random.sample(exercise_list, 3)
print(random_elements)

# Случайный выбор 3-х элементов из списка с повторениями
random_elements = random.choices(exercise_list, k=3)
print(random_elements)


