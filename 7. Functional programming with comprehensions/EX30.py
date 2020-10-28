def flatten(list_of_lists):
    return [one_el
            for one_sublist in list_of_lists  # Iterates through each element of list_of_lists
            for one_el in one_sublist]  # Iterates through each element of one_sublist


print(flatten([[1, 2], [3, 4]]))
