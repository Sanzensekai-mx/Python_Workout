import random


def password_generator(str_passwd_symbols):
    def create_passwd(length):
        output = []
        for sym in range(length):
            output.append(random.choice(str_passwd_symbols))
        return ''.join(output)

    return create_passwd


# alpha_password = password_generator('abcdef')
# symbol_password = password_generator('!@#$%')
# print(alpha_password(5))
# print(alpha_password(10))
# print(symbol_password(5))
# print(symbol_password(10))


#  EX27_1


def create_passwd_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def take_passwd(check_this_passwd):
        uppercase, lowercase, punctuation, digits = [], [], [], []
        for el in check_this_passwd:
            if el in 'abcdefghijklmnopqrstuvwxyz':
                lowercase.append(el)
            elif el in 'abcdefghijklmnopqrstuvwxyz'.upper():
                uppercase.append(el)
            elif el in '.,&!@#$;:\'\"\\/()[]`~№^*':
                punctuation.append(el)
            elif el in '0123456789':
                digits.append(el)
        output = {'uppercase': min_uppercase <= len(uppercase), 'lowercase': min_lowercase <= len(lowercase),
                  'punctuation': min_punctuation <= len(punctuation), 'digits': min_digits <= len(digits)}
        for k, v in output.items():
            print(f'{k} -- {v}')
        return True if False not in output.values() else False

    return take_passwd


my_password = 'Mac.MarMok1357!!!'
not_my_password = 'macMae1'


# print(create_passwd_checker(3, 4, 2, 2)(my_password))
# print(create_passwd_checker(3, 4, 2, 2)(not_my_password))


#  27_2 like itemgetter


def get_item(arg):
    def func(data_structure):
        return data_structure[arg]

    return func


d = {'a': 1, 'b': 2}
f = get_item('a')
# print(f(d))
# print(get_item('b')(d))


#  27_3

def f1(num):
    return 5 + num


def f2(num):
    return num + 100


def do_both(func1, func2):
    def g(arg):
        return func2(func1(arg))

    return g


x = 10
print(f2(f1(x)))
print(do_both(f1, f2)(x))
