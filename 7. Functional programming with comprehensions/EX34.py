def get_cv(file_name):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip() for word in open(file_name) if vowels < set(word.lower())}


print(get_cv('words.txt'))
