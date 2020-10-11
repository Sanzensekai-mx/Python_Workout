def my_xml(tag_name, content='', **kwargs):
    attr = "".join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tag_name}{attr}>{content}</{tag_name}>'


# print(my_xml('foo'))
# print(my_xml('foo', 'bar'))
# print(my_xml('foo', 'bar', a=1, b=2, c=3))


#  EX25_1


def copy_file(input_file_name, *args):
    for file in args:
        with open(input_file_name, 'r', encoding='utf-8') as in_file:
            with open(file, 'w', encoding='utf-8') as to_file:
                for line in in_file:
                    to_file.write(line)


copy_file('stix6.txt', 'stix6_1.txt', 'stix6_2.txt')
