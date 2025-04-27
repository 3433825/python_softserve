def count_words(sentence):
    words = sentence.split()  # Розділити речення на слова за пробілами
    return len(words)


sentence = "In this written assignment I will try to describe a very recent event in our life. This event  "
print(len(sentence.split()))
