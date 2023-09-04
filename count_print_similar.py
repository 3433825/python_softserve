from string import punctuation
from Data import data


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

# print(find_simil_words(data.SENTENCE))