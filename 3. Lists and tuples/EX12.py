import collections

words = ['this', 'is', 'an', 'elementary', 'test', 'example']


def most_repeating_letter_count(word):
    return collections.Counter(word).most_common(1)[0][1]


def most_repeating_word(sequence_of_strings):
    return max(sequence_of_strings, key=most_repeating_letter_count)


def most_repeating_word_2(sequence_of_strings):
    return sorted(sequence_of_strings, key=most_repeating_letter_count)[-1]


# print(most_repeating_word(words))

# 1


def most_repeating_vowel_count(word):
    list_most = collections.Counter(word).most_common()
    list_most_vowel = []
    for el in range(len(list_most)):
        if list_most[el][0] not in 'aoiuey':
            continue
        list_most_vowel.append(el)
    return list_most_vowel[0][1]


def most_repeating_vowels(sequence_of_strings):
    return max(sequence_of_strings, key=most_repeating_letter_count)


words1 = ['aaaaeey', 'aey', 'eee']

# print(most_repeating_vowels(words1))
