d = {'a': 1, 'b': 2, 'c': 3}


def flip_dict(input_dict):
    # return {d[key]: key for key in d.keys()}
    return {value: key for key, value in d.items()}


# print(flip_dict(d))

#  EX32_1
example_str = 'this is an easy test'


def count_vowels_in_words_in_str(string):
    return {word: len([i for i in word if i in 'aeoiuy']) for word in string.split()}


print(count_vowels_in_words_in_str(example_str))
