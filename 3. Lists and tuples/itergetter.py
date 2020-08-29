import operator

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]

s = 'abcdef'
t = (10, 20, 30, 40, 50, 60)
get_last_first = operator.itemgetter(2, 4)
print(get_last_first(s))


def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))


print(alphabetize_names(PEOPLE))
for p in sorted(PEOPLE, key=operator.itemgetter('last', 'first')):
    print(f'{p["last"]}, {p["first"]}: {p["email"]}')
