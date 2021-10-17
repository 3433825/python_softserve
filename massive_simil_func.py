def simil_words_ru(text):
    """Make massive similar words"""

    from difflib import SequenceMatcher
    from string import punctuation

# Making list of words
    words = []
    for word in text.lower().split():
        word_without_punctuation = word.strip(punctuation)
        if word_without_punctuation:
            words.append(word_without_punctuation)

#Making list of similar words
    numbers = list(range(0, len(words)))
    similar_words = []
    coincidence = 0.8
    for number in numbers:
        similar_words.append([])
        similar_words[number].append(words[number])
        for number2 in numbers:
            ratio = SequenceMatcher(None,words[number], words[number2]).ratio()
            if ratio >= coincidence:
                if number != number2:
                    similar_words[number].append(words[number2])
    return similar_words
