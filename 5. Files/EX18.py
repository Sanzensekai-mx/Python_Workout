import os


def get_final_line(filename):
    with open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
        final_line = ''
        for line in f:
            final_line = line
        return final_line


# print(get_final_line('stix.txt'))

# 18_1

def get_sum_of_numbers_in_file(filename):
    with open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
        sum_num_file = 0
        for line in f:
            splitting_line = line.split()
            for string in splitting_line:
                try:
                    sum_num_file += int(string.strip(',.?;:'))
                except ValueError:
                    continue
        return sum_num_file


# print(get_sum_of_numbers_in_file('stix.txt'))


# 18_2

def collum_2(file_with_cols):
    all_sum = 0
    with open(file_with_cols, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                split_line = list(map(int, line.split('\t')))
                result_line = split_line[0] * split_line[1]
            except ValueError:
                continue
            print(result_line)
            all_sum += result_line
    print(f'sum - {all_sum}')


collum_2('for_18_2.txt')