import os
import collections


def get_rainfall():
    rainfall = {}
    while True:
        city_input = input('Enter city\'s name: ')
        if not city_input:
            break
        try:
            mm_input = int(input('Enter mm input: '))
        except ValueError:
            print('You didn\'t enter a valid integer; try again.')
            continue
        rainfall[city_input] = rainfall.get(city_input, 0) + mm_input
    for city, rain in rainfall.items():
        print(f'{city} - {rain}')


# get_rainfall()


def get_rainfall_2():
    rainfall = {}
    while True:
        city_input = input('Enter city\'s name: ').strip()
        if not city_input:
            break
        try:
            mm_input = int(input('Enter mm input: '))
        except ValueError:
            print('You didn\'t enter a valid integer; try again.')
            continue
        rainfall[city_input] = rainfall.get(city_input, [])
        rainfall[city_input].append(mm_input)
    for city, rain in rainfall.items():
        print(f'{city}: total - {sum(rain)}, average - {sum(rain) / len(rain)}')


# get_rainfall_2()

def get_lens_words(file):
    result_dict = collections.defaultdict(list)
    with open(os.path.join(os.getcwd(), file), 'r', encoding='utf-8') as f:
        for lines in f:
            for word in lines[:-2].split():
                result_dict[len(word)].append(word) if word[-1] not in '.,:;?!' else \
                    result_dict[len(word[:-1])].append(word[:-1])
    return result_dict


print(get_lens_words('stix.txt'))


