def transform_values(func, input_dict):
    return {key: func(value) for key, value in input_dict.items()}


d = {'a': 1, 'b': 2, 'c': 3}


# print(transform_values(lambda x: x * x, d))


# EX33_1
# Дебильное упражнение, непонятное нихуя
# EX33_2

def passwd_to_dict(passwd_file):
    return {user_name: user_id for string in open(passwd_file)
            for user_name, user_id in {string.split(':')[0]: string.split(':')[2]}.items()}


print(passwd_to_dict('passwd'))
