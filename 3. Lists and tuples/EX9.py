def first_last(type_data):
    return type_data[::len(type_data) - 1]


print(first_last('abc'))
print(first_last([1, 2, 3, 4]))
