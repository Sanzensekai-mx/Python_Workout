import csv


def passwd_to_csv(passwd_style_file, new_csv_file):
    with open(passwd_style_file, 'r') as passwd_file, open(new_csv_file, 'w') as output_file:
        infile = csv.reader(passwd_file, delimiter=':')
        outfile = csv.writer(output_file, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))


passwd_to_csv('passwd', 'output.csv')
