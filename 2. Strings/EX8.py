def str_sort(string):
    return ''.join(sorted(string))


# print(str_sort('bca'))


def str_name(names):
    return ', '.join(sorted(names.split(' ')))


print(str_name('Tom Dick Harry'))


def last_word_alpha(names):
    return sorted(names.split(' '))[-1]


print(last_word_alpha('Tom Dick Harry'))


def max_len(names):
    return sorted(names.split(' '), key=len)[-1]


print(max_len('Tom Dick Harry'))
