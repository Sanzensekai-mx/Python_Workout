def flatten(list_of_lists):
    return [one_el
            for one_sublist in list_of_lists  # Iterates through each element of list_of_lists
            for one_el in one_sublist]  # Iterates through each element of one_sublist


# print(flatten([[1, 2], [3, 4]]))


# EX31_1


def flatten_odd_ints(list_of_lists):
    return [one_el for one_sublist in list_of_lists
            for one_el in one_sublist if type(one_el) == int and one_el % 2 != 0]


print(flatten_odd_ints([[1, 2], [3, 4]]))
print(flatten_odd_ints([[1, 2, 3.0], [13, 80.1], ['string', 5]]))
