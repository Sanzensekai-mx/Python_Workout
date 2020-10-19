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


print(sum_hex_num(['0x3e8', '0x7', '0x3f', '0xff']))
