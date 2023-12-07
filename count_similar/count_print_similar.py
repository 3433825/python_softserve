import timeit
from string import punctuation
from Data import data
from Fibonacci.duration import duration
from collections import Counter


def find_simil_words(text: str):
    """Make massive similar words"""
    # Making list of words
    words = text.lower().split()
    words = list(map(lambda word: word.strip(punctuation), words))

    #Making dict similar words
    word_counts = {}

    # Перебираем каждое слово в предложении
    for word in words:
        # Используем метод get() словаря для увеличения счетчика вхождений слова
        word_counts[word] = word_counts.get(word, 0) + 1

    # Формируем список повторяющихся слов
    duplicates = [word for word, count in word_counts.items() if count > 1]
    duplicates_count = [(word, count) for word, count in word_counts.items() if count > 1]

    return word_counts, duplicates, duplicates_count


words_set, duplicates_words, duplicates_words_count = find_simil_words(data.SENTENCE)
for key_value in words_set.items():
    print(key_value)
for w in duplicates_words:
    print(w)
for t in duplicates_words_count:
    print(t)


text = data.SENTENCE
print(find_simil_words(data.SENTENCE))
print()
execution_time = timeit.timeit(lambda: find_simil_words(text), number=1)
print(f"execution_time with timeit module: {execution_time:.6f} s")
print()


@duration
def count_similar_words_ru(text):
    return find_simil_words(text)
print(count_similar_words_ru(text))
# *************************************************************************************************

"""
from collections import Counter

def sort_least_repeated(array):
    counter = Counter(array)  # Подсчет числа вхождений каждого элемента
    least_repeated = sorted(counter.items(), key=lambda x: (x[1], -x[0]))  # Сортировка по наименее встречаемым
    элементам

    sorted_array = []
    for element, count in least_repeated:
        sorted_array.extend([element] * count)  # Добавление элементов в результирующий массив в соответствии с их
                                                # количеством

    return sorted_array
Вызов функции sort_least_repeated с массивом целых чисел k вернет отсортированный массив с наименее повторяющимися
числами. Если несколько чисел имеют одинаковое количество повторений, они будут отсортированы в порядке убывания.

"""


sentence_inst = data.SENTENCE


def find_duplicated_words(sentence):
    """Make massive similar words"""
    # Making list of words
    words = sentence.lower().split()
    words = list(map(lambda word: word.strip(punctuation), words))

    # Making dict similar words
    counter = Counter(words)  # Подсчет числа вхождений каждого элемента
    duplicated_words = [element for element, count in counter.items() if count > 1]  # Добавление элементов в
        # результирующий массив в соответствии с их количеством
    duplicated_words_dict = {element: count for element, count in counter.items() if count > 1}

    return duplicated_words, duplicated_words_dict


duplicated_words = find_duplicated_words(sentence_inst)[0]
print(duplicated_words)
print(find_duplicated_words(sentence_inst)[1])


@duration
def find_duplicated_words_ru(text):
    return find_duplicated_words(text)
print(find_duplicated_words_ru(text))
