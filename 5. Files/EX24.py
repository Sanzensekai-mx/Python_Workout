import csv
import collections


def reverse_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_file, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            out_f.write(f'{line.rstrip()[::-1]}\n')


# reverse_lines('stix.txt', 'stix_reverse_lines.txt')


#  EX24_1


def encrypt_with_ord(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_file, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            for char in line:
                out_f.write(f'{ord(char)} ')
            out_f.write('\n')


def decrypt_with_char(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_file, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            line = line.split(' ')
            for one_ord in line:
                out_f.write(f'{chr(int(one_ord))}') if one_ord != '\n' else None
        out_f.write('\n')


# encrypt_with_ord('stix.txt', 'stix_ex24_1_encrypt_ord.txt')
# decrypt_with_char('stix_ex24_1_encrypt_ord.txt', 'stix_ex24_1_decrypt_char.txt')


#  EX24_2


def leave_vowels_not_vowels(input_file, output_vowels, output_not_vowels):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_vowels, 'w', encoding='utf-8') as out_v, open(
            output_not_vowels, 'w', encoding='utf-8') as out_not_v:
        for line in in_f:
            for char in line:
                if char in 'aeouiyауеоияыюэ.,?!;:':
                    out_v.write(char)
                if char not in 'aeouiyaeouiyауеоияыюэ':
                    out_not_v.write(char)
            out_v.write('\n')


# leave_vowels_not_vowels('stix.txt', 'stix_only_vowels.txt', 'stix_only_not_vowels.txt')


#  EX24_3


def users_use_this_shell(passwd_file, outfile):
    with open(passwd_file, 'r', encoding='utf-8') as passwd, open(outfile, 'w', encoding='utf-8') as out:
        passwd = csv.reader(passwd, delimiter=':')
        result_dict = collections.defaultdict(list)
        for line in passwd:
            result_dict[line[-1]].append(line[0])
        for shell, names in result_dict.items():
            out.write(f'{shell}: {" ".join(names)}\n')


users_use_this_shell('passwd', 'passwd_ex24_3.txt')
