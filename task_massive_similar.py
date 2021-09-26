from difflib import SequenceMatcher
from string import punctuation
# import re

words = []
text = 'Он вышел погулять в "лес". В лесу он встретил ее. ' \
       'Она тоже вышла погулять, погода была хорошая.'
# text = re.sub(r'[.\,\?\!\;\:\"\&\*\@\#\$\%\^\(\)\=]','', text)

for word in text.lower().split():
    word_without_punctuation = word.strip(punctuation)
    if word_without_punctuation:
        words.append(word_without_punctuation)

numbers = list(range(0, len(words) - 2))
number2s = list(range(1, len(words)))
similar_words = []

for number in numbers:
    similar_words.append([])
    similar_words[number].append(words[number])
    for number2 in number2s:
        ratio = SequenceMatcher(None,words[number], words[number2]).ratio()
        if ratio >= 0.8:
            if number != number2:
                similar_words[number].append(words[number2])

print(text)
print(words)
print(similar_words)
for i in list(range(len(similar_words))):
    print(f'\n {similar_words[i]}')
