d = {'a': 1, 'b': 2, 'c': 3}


def flip_dict(input_dict):
    # return {d[key]: key for key in d.keys()}
    return {value: key for key, value in d.items()}


print(flip_dict(d))
