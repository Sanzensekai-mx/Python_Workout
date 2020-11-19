import string


def gematria_dict():
    return {char: index for index, char in enumerate(string.ascii_lowercase, 1)}


# print(gematria_dict())


# EX35a_1


def config_to_dict(filename):
    return {key.strip(): value.strip() for string in open(filename)
            for key, value in {string.split('=')[0]: string.split('=')[1]}.items()}


# print(config_to_dict('config.txt'))


# EX35a_2

def config_to_dict_expand(filename):
    return {key.strip(): int(value.strip()) for string_i in open(filename)
            for key, value in {string_i.split('=')[0]: string_i.split('=')[1]}.items() if value.strip().isdigit()}


print(config_to_dict_expand('config.txt'))
