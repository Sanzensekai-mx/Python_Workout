def reverse_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_file, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            out_f.write(f'{line.rstrip()[::-1]}\n')


reverse_lines('stix.txt', 'stix_reverse_lines.txt')