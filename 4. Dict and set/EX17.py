def how_many_different_numbers(list_of_num):
    return len(set(list_of_num))


numbers = [1, 2, 3, 1, 2, 3, 4, 1]
# print(how_many_different_numbers(numbers))


# unique_numbers = set()
# for number in numbers:
#     unique_numbers.add(number)
#
# unique_numbers = set()
# unique_numbers.update(numbers)
#
# unique_numbers = {*numbers}
# print(unique_numbers)
