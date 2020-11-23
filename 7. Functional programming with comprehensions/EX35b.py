import string


def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}


def gematria_for(string_):
    return sum(gematria_dict().get(char, 0) for char in string_)


def gematria_equal_words(string_):
    score = gematria_for(string_.lower())
    return [word.strip() for word in open('words.txt') if gematria_for(word.lower()) == score]


print(gematria_equal_words('cat'))
