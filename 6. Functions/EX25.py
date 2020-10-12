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


# copy_file('stix6.txt', 'stix6_1.txt', 'stix6_2.txt')


#  EX25_2


def factorial_like_func(*args):
    result = 0
    for arg in args:
        if args.index(arg) == 0:
            result += arg
        result *= arg
    return result


# print(factorial_like_func(0, 0, 0, 0, 0))
# print(factorial_like_func(1, 2, 3, 4, 5))
# print(factorial_like_func(1, 2))
# print(factorial_like_func(10, 20, 30))
# print(factorial_like_func(0, 1, 2))


#  EX25_3

def any_join(data, glue=" "):
    transform_data_to_str = [str(i) for i in data]
    result = ''
    for el in transform_data_to_str:
        if el == transform_data_to_str[-1]:
            result += el
            break
        result += el + glue
    return result


print(any_join([1, 2, 3]))
print(any_join(['a', 'b', 'c'], '**'))
print(any_join('abc', '**'))
