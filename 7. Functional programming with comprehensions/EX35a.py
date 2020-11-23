import string
import json


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


# print(config_to_dict_expand('config.txt'))


# EX35a_2


def transform_json_to_dict(json_file):
    # Название, население в дикт
    return {name_city: population_city for dictionary in json.load(open(json_file))
            for name_city, population_city in {dictionary['city']: dictionary['population']}.items()}


def transform_json_to_another_dict(json_file):
    return {(city_state, name_city): population_city for dictionary in json.load(open(json_file))
            for name_city, population_city in {dictionary['city']: dictionary['population']}.items()
            for city_state in {None: dictionary['state']}.values()}


print(transform_json_to_dict('cities.json'))
print(transform_json_to_another_dict('cities.json'))
print(len(transform_json_to_dict('cities.json')))
print(len(json.load(open('cities.json'))))