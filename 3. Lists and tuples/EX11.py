import operator
PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]

# s = 'abcdef'
# t = (10, 20, 30, 40, 50, 60)
# get_last_first = operator.itemgetter(2, 4)
# print(get_last_first(s))


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


# print(alphabetize_names(PEOPLE))
# for p in sorted(PEOPLE, key=operator.itemgetter('last', 'first')):
#     print(f'{p["last"]}, {p["first"]}: {p["email"]}')


def positive_negative_sort(list_of_int):
    return sorted(list_of_int, key=abs)
    # return sorted(list_of_int)


# print(positive_negative_sort([-1, 29, 34, -56, -30, 10, 4, -6, -8, 13, -67]))


def len_vowels(string):
    vowels = []
    for c in string:
        if c in 'aoieuy':
            vowels.append(c)
    return len(vowels)


def vowels_count_sort(list_of_str):
    return sorted(list_of_str, key=len_vowels)


# print(vowels_count_sort(['hello', 'whaats', 'aye', 'vowels', 'real me', 'low']))


def sort_by_sum(list_of_lists):
    return sorted(list_of_lists, key=sum)


print(sort_by_sum([
    [1, 2, 3, 8],
    [],
    [56, 0, 9],
    [16, 78],
    [10, 11]
]))
