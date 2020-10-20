import operator

# map
words = 'this is a bunch of words'.split()
x = map(len, words)
print(sum(x))

# filter
words = 'this is a bunch of words'.split()


def is_a_long_word(one_word):
    return len(one_word) > 4


x = filter(is_a_long_word, words)
print(' '.join(x))

# map with operator.mul
letters = 'abcd'
numbers = range(1, 5)
x = map(operator.mul, letters, numbers)
print(' '.join(x))

# map with operator.mul and comprehension
letters = 'abcd'
numbers = range(1, 5)
print(' '.join(operator.mul(one_letter, one_number) for one_letter, one_number in zip(letters, numbers)))

# map and filter
print(list(map(lambda x: f'{x} Ivan', filter(is_a_long_word, words))))
