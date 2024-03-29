import operator
import collections
import pprint


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


# print(func_file('stix.txt', pl_word))


# EX31_2


list_of_dicts = [{'name': 'Ivan', 'age': '20'}, {'name': 'El', 'age': '21'}, {'name': 'Mica', 'age': '18'},
                 {'name': 'Kl', 'age': '12'}]
# print([(name, value) for dict_in_list in list_of_dicts for name, value in dict_in_list.items()])

#  EX31_3


list_of_dicts = [{'name': 'Ivan', 'hobbies': 'programming'}, {'name': 'El', 'hobbies': 'programming'},
                 {'name': 'Mica', 'hobbies': 'draw'},
                 {'name': 'Kl', 'hobbies': 'draw'}, {'name': 'KlS', 'hobbies': 'draw'},
                 {'name': 'KlS', 'hobbies': 'listen music'}, {'name': 'KlSLM', 'hobbies': 'listen music'},
                 {'name': 'MLKlS', 'hobbies': 'write'}]

# result_dict = collections.Counter([dict_in_list.get('hobbies') for dict_in_list in list_of_dicts])

result_list = sorted([(name, int(value)) for name, value in collections.Counter([dict_in_list.get('hobbies')
                                                                         for dict_in_list in list_of_dicts]).items()])
for hobby in [cortezh[0] for cortezh in result_list[:3]]:
    print(hobby)