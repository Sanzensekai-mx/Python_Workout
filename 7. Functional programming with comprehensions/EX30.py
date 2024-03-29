import operator


def flatten(list_of_lists):
    return [one_el
            for one_sublist in list_of_lists  # Iterates through each element of list_of_lists
            for one_el in one_sublist]  # Iterates through each element of one_sublist


# print(flatten([[1, 2], [3, 4]]))


# EX30_1


def flatten_odd_ints(list_of_lists):
    return [one_el for one_sublist in list_of_lists
            for one_el in one_sublist if type(one_el) == int and one_el % 2 != 0]


# print(flatten_odd_ints([[1, 2], [3, 4]]))
# print(flatten_odd_ints([[1, 2, 3.0], [13, 80.1], ['string', 5]]))

#  EX30_2


child_grandchildren = {'A': ['B', 'C', 'D'], 'E': ['F', 'G']}
# print([one_grandchild for one_child in child_grandchildren.values() for one_grandchild in one_child])


#  EX30_3

child_grandchildren = {'Igor': [{'name': 'Ivan', 'age': '20'}, {'name': 'El', 'age': '21'}],
                       'Liza': [{'name': 'Mica', 'age': '18'}, {'name': 'Kl', 'age': '12'}]}
lst_merge = []
[lst_merge.append(dict_grand_child) for one_child in [one_child for one_child in child_grandchildren.values()]
 for dict_grand_child in one_child]
print(sorted(lst_merge, key=lambda x: x['age']))
print([one_grand_name['name'] for one_grand_name in sorted(lst_merge, key=lambda x: x['age'])])
