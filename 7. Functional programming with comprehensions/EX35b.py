import string
import pprint


def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}


GEMATRIA = gematria_dict()


def gematria_for(string_):
    return sum(GEMATRIA.get(char, 0) for char in string_)


def gematria_equal_words(string_):
    score = gematria_for(string_.lower())
    return [word.strip() for word in open('words.txt') if gematria_for(word.lower()) == score]


# print(gematria_equal_words('cat'))


# EX35b_1

fahrenheit_city = {'Moscow': 30, 'Ulyanovsk': 25}
new_dict = {city: ((value - 32) * 5) // 9 for city, value in fahrenheit_city.items()}

# print(new_dict)

# EX35b_2

list_of_tuple = [('Artur Kon', 'Star Wars', 5), ('Dantes Broudi', 'keep calm', 10),
                 ('Reuven Lerner', 'Python Workout', 12)]
book_dict = {book_title: {'author’s first name': author.split(' ')[0],
                          'the author’s last name': author.split(' ')[1].strip(),
                          'cost': cost}
             for one_tuple in list_of_tuple for author, book_title in {one_tuple[0]: one_tuple[1]}.items()
             for cost in {None: one_tuple[2]}.values()}

# pprint.pprint(book_dict)


# EX35b_3

dollars_in_not_dollars = {'RUB': 75.56, 'EUR': 0.8417, 'GBP': 0.7484}


def transform_dollars_to():
    while True:
        user_input = input('--> ')
        if user_input not in dollars_in_not_dollars.keys():
            print('try again')
            continue
        break
    return {book_title: {'author’s first name': author.split(' ')[0],
                         'the author’s last name': author.split(' ')[1].strip(),
                         'cost': cost}
            for one_tuple in list_of_tuple for author, book_title in {one_tuple[0]: one_tuple[1]}.items()
            for cost in {None: round(one_tuple[2] * dollars_in_not_dollars.get(user_input), 2)}.values()}


print(transform_dollars_to())
