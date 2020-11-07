def pl_word(word):
    if word[0] in 'aeouiyAEOUYI':
        return f'{word}way'
    return f'{word[1:]}{word[0]}way'


def pl_file(filename):
    return ' '.join(pl_word(one_word)
                    for one_line in open(filename)  # Iterates through each line of filename
                    for one_word in one_line.split())  # Iterates through each word in the current line


# print(pl_word('Milk'))
# print(pl_file('stix.txt'))


# EX31_1


def func_file(filename, func):
    return ' '.join(func(one_word)
                    for one_line in open(filename)
                    for one_word in one_line.split())


print(func_file('stix.txt', pl_word))
