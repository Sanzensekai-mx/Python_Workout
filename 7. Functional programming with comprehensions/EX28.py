def join_numbers(range_of_nums):
    return ', '.join([str(num) for num in range_of_nums])


print(join_numbers(range(15)))
