import os


def get_final_line(filename):
    with open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
        final_line = ''
        for line in f:
            final_line = line
        return final_line


print(get_final_line('stix.txt'))
