def join_numbers(range_of_nums):
    return ', '.join([str(num) for num in range_of_nums])


# print(join_numbers(range(15)))


#  EX28_1


def join_numbers_2(range_of_nums):
    return ', '.join([str(num) for num in range_of_nums if num in range(11)])


print(join_numbers_2(range(15)))
