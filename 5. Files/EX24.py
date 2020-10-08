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


encrypt_with_ord('stix.txt', 'stix_ex24_1_encrypt_ord.txt')
decrypt_with_char('stix_ex24_1_encrypt_ord.txt', 'stix_ex24_1_decrypt_char.txt')
