def dict_diff(dict1, dict2):
    output = {}
    all_keys = dict1.keys() | dict2.keys()
    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            output[key] = [dict1.get(key), dict2.get(key)]
    return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
d5 = {'a': 1, 'b': 2, 'd': 4}


# print(dict_diff(d1, d2))
# print(dict_diff(d3, d4))
# print(dict_diff(d1, d5))


def dict_sum(*args):
    output = {}
    for el_dict in args:
        for key, value in el_dict.items():
            if output.get(key) not in output.keys():
                output[key] = value
    return output


# print(dict_sum(d1, d2, d3, d4, d5))
di1 = {'Ivan': 4, 'Akina': 5}
di2 = {'Ivan': 10, 'Akina': 8, 'Ann': 9}
di3 = {'Ivan': 3}


# print(dict_sum(di1, di2, di3))


def dict_even_odd(*args):
    if len(args) % 2 == 0:
        even = list(args)[1::2]
        odd = list(args)[::2]
        output_dict = {}
        for a in range(len(args) // 2):
            output_dict[odd[a]] = even[a]
        return output_dict


# print(dict_even_odd('a', 1, 'b', 2))
# print(dict_even_odd('Pep', 132, 31, 'ad'))


def func_for_ex(*args):
    if len(args) == 2:
        if type(args[0]) == str and type(args[1]) == str:
            return True
        else:
            return False


def dict_partition(d, f):
    first_true = {}
    second_false = {}
    for k, v in d.items():
        sol = f(k, v)
        if sol:
            first_true[k] = v
        else:
            second_false[k] = v
    return first_true, second_false


print(dict_partition({'first': 1, 'second': 'two', 'third': '3'}, func_for_ex))
# В данном случае функция определит пару, в которой и ключ, и значение стринговые, потом добавит эти пары в first_true
# Остальные пойдут в second_false
