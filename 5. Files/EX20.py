import os


def wordcount(file):
    num_char = 0
    num_words = 0
    num_lines = 0
    num_unique_words = 0
    list_of_words = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            num_lines += 1
            for word in line.split():
                num_words += 1
                if word not in list_of_words:
                    num_unique_words += 1
                list_of_words.append(word)
            for char in line:
                # if char != ' ':
                num_char += 1
    print(f'''
num char - {num_char}
num words - {num_words}
num lines - {num_lines}
num unique words - {num_unique_words}
''')


# wordcount('stix.txt')
# wordcount('wcfile.txt')


def wordcount_sol(filename):
    counts = {'characters': 0,
              'words': 0,
              'lines': 0}
    unique_words = set()
    for one_line in open(filename):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())
        counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')


# wordcount_sol('wcfile.txt')

# EX20_1


def count_specific_words(file_name, *args):
    count_result = {}
    for arg in args:
        count_result[arg] = 0
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if word.strip(',!?;:.') in args:
                    count_result[word.strip(',!?;:.')] += 1
    return count_result


# for k, v in count_specific_words('stix.txt', 'и', 'Пусть', 'не', 'рна').items():
#     print(f'{k} - {v}')


# EX20_2


def return_files_sizes():
    file_sizes = {}
    for name_file in os.listdir():
        file_sizes[name_file] = os.stat(os.path.join(os.getcwd(), name_file)).st_size
    return file_sizes


# for k, v in return_files_sizes().items():
#     print(f'{k} - {v} байт')


# EX20_3


def count_each_letter_files(dir_path):
    count_letters = {}
    os.chdir(dir_path)
    for file in os.listdir(dir_path):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                for letter in line.lower():
                    if letter in '.?!,;:\n\t*^$@%()_-+=\\/][{}\'\"# —«»':
                        continue
                    if letter not in count_letters.keys():
                        count_letters[letter] = 0
                    count_letters[letter] += 1

    return count_letters


print(count_each_letter_files(os.path.join(os.getcwd(), 'dir_for_EX20_3')))
