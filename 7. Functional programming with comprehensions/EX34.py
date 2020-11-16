def get_cv(file_name):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip() for word in open(file_name) if vowels < set(word.lower())}


# print(get_cv('words.txt'))


# EX34_1


def get_user_shell(passwd_file):
    return {string.strip().split(':')[-1] for string in open(passwd_file)}


# print(get_user_shell('passwd'))


# EX34_2


def get_length(file_name):
    return {len(word.strip()) for word in open(file_name)}


print(get_length('words.txt'))
print(get_length('stix.txt'))