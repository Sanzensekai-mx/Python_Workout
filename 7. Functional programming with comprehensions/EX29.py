def sum_numbers(string):
    return sum([int(i) for i in string.split() if i.isdigit()])


# print(sum_numbers('10 abc 20 de44 30 55fg 40'))

#  EX29_1


# with open('stix.txt', 'r', encoding='utf-8') as f:
    # for line in [i.strip('\n') for i in f if len(i) > 20]:
        # print(line) if [vowel for vowel in line if vowel in 'aeiouy'] else None


#  EX29_2


def covert_phone_num(list_of_num):
    result_list = []
    for i in [num.split('-') for num in list_of_num]:
        result_list.append(f'{str(int(i[0]) + 1)}-{i[1]}-{i[2]}') if i[1][0] in '012345' \
            else result_list.append(f'{i[0]}-{i[1]}-{i[2]}')
    return result_list


print(covert_phone_num(['123-456-7890', '123-333-4444', '123-777-8888']))
