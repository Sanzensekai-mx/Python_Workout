import os


def get_final_line(filename):
    with open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
        final_line = ''
        for line in f:
            final_line = line
        return final_line


# print(get_final_line('stix.txt'))


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


print(get_sum_of_numbers_in_file('stix.txt'))
