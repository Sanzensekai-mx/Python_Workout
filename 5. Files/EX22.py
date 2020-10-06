import csv


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
                    outfile.writerow((record[i] for i in user_input))
                except IndexError:
                    print('The entered index exceeds the maximum index of the passwd file!!!')
                    break


passwd_to_csv_user_fields('passwd', 'output_ex22_1.csv')
