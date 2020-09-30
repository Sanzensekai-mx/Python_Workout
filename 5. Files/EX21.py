import os
import hashlib


def find_longest_word(file_name):
    result = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if len(word) > len(result):
                    result = word.strip()
    return result


def find_all_longest_words(dir_name):
    return {filename: find_longest_word(os.path.join(os.getcwd(), dir_name, filename))
            for filename in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, filename))}


# print(find_all_longest_words('dir_for_EX20_3'))


# EX21_1

def use_md5(dir_name):  # path to file
    result = {}
    for file in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name, file)):
            result[file] = ''
            with open(os.path.join(dir_name, file), 'r', encoding='utf-8') as f:
                for line in f:
                    result[file] += line
                result[file] = hashlib.md5(result[file].encode()).hexdigest()
    return result


print(use_md5(os.path.join(os.getcwd())))
print(use_md5(os.path.join(os.getcwd(), 'dir_for_EX20_3')))
