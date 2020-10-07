import csv
import random


def passwd_to_csv(passwd_style_file, new_csv_file):
    with open(passwd_style_file, 'r') as passwd_file, open(new_csv_file, 'w') as output_file:
        infile = csv.reader(passwd_file, delimiter=':')
        outfile = csv.writer(output_file, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


# passwd_to_csv('passwd', 'output.csv')


#  EX22_1


def passwd_to_csv_user_fields(passwd_style_file, new_csv_file):
    user_input = [int(i) for i in input('Enter a list of field numbers separated by spaces (0-6): ').split()]
    with open(passwd_style_file, 'r') as passwd_file, open(new_csv_file, 'w') as output_file:
        infile = csv.reader(passwd_file, delimiter=':')
        outfile = csv.writer(output_file, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                try:
                    outfile.writerow((record[i].strip('.,!?') for i in user_input))
                except IndexError:
                    print('The entered index exceeds the maximum index of the passwd file!!!')
                    break


# passwd_to_csv_user_fields('passwd', 'output_ex22_1_ex23_1.csv')


# EX22_2
user = {'Ivan': 'qwerty', 'Andri': '1234', 'K': 'first', 'DD-walker': 1000, 'DD-dog': [1, 23, 34],
        'Marina': {1: 2, 2: 3}}


def dict_to_csv(dict_csv):
    with open('csv_from_dict_ex22_2.csv', 'w', encoding='utf-8') as output:
        output = csv.writer(output, delimiter='\t')
        for k, v in dict_csv.items():
            output.writerow((k, v, type(v)))


# dict_to_csv(user)


#  EX22_3


def sum_random_num_in_csv_file(csv_file):
    with open(csv_file, 'w', encoding='utf-8') as write_f:
        write_f = csv.writer(write_f, delimiter=' ')
        for line in range(10):
            write_f.writerow((random.randint(10, 100) for i in range(10)))
    with open(csv_file, 'r', encoding='utf-8') as read_f:
        read_f = csv.reader(read_f, delimiter=' ')
        for line in read_f:
            # print(line)
            line_list = [int(i) for i in line]
            if len(line) > 1:
                print(f'sum: {sum(line_list)}  average: {sum(line_list)/len(line_list)}')


sum_random_num_in_csv_file('csv_ex22_3.csv')
