def sum_numbers(string):
    return sum([int(i) for i in string.split() if i.isdigit()])


# print(sum_numbers('10 abc 20 de44 30 55fg 40'))

#  EX29_1


with open('stix.txt', 'r', encoding='utf-8') as f:
    for line in [i.strip('\n') for i in f if len(i) > 20]:
        print(line) if [vowel for vowel in line if vowel in 'aeiouy'] else None
