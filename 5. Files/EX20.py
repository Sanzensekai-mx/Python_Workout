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


wordcount_sol('wcfile.txt')
