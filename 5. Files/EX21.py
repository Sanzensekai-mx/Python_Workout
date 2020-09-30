import os


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


print(find_all_longest_words('dir_for_EX20_3'))
