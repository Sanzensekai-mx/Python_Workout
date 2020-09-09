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


print(dict_sum(d1, d2, d3, d4, d5))
di1 = {'Ivan': 4, 'Akina': 5}
di2 = {'Ivan': 10, 'Akina': 8, 'Ann': 9}
di3 = {'Ivan': 3}
print(dict_sum(di1, di2, di3))
