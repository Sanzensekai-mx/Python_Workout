def join_numbers(range_of_nums):
    return ', '.join([str(num) for num in range_of_nums])


# print(join_numbers(range(15)))


#  EX28_1


def join_numbers_2(range_of_nums):
    return ', '.join([str(num) for num in range_of_nums if num in range(11)])


# print(join_numbers_2(range(15)))


#  EX28_2

def sum_hex_num(list_hex_str):
    return sum([int(hex_str, 16) for hex_str in list_hex_str])


# print(sum_hex_num(['0x3e8', '0x7', '0x3f', '0xff']))


#  EX28_3

# ?????
def reverse_comprehension(text_file):
    with open(text_file, 'r') as f:
        return [' '.join(line.split()[::-1]) for line in f for line in line.splitlines()]


print(reverse_comprehension('text_file_for_ex28_3.txt'))
