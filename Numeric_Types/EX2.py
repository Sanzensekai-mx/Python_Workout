def my_sum(*args):
    output = 0
    for i in args:
        output += i
    return output


print(my_sum(1, 2, 5, 3))
print(my_sum(*[1, 2, 5, 3]))


def my_sum2(list_arg, dop_arg=0):
    output = 0 + dop_arg
    for i in list_arg:
        output += i
    return output


print(my_sum2([1, 2, 5, 3], 2))


def average_fu(list_arg):
    sum_list = 0
    for i in list_arg:
        sum_list += i
    return sum_list / len(list_arg)


print(f'The average number is {average_fu([1, 2, 5, 3])}')


def words_list(list_words):
    len_words = []
    for word in list_words:
        len_words.append(len(word))
    min_len, max_len, average_len = min(len_words), max(len_words), sum(len_words) / len(len_words)
    return min_len, max_len, average_len


print(words_list(['car', 'toys', 'boyzz']))


def sum_only_int_float(list_objects):
    sum_output = 0
    for obj in list_objects:
        if type(obj) == int or type(obj) == float:
            sum_output += obj
    return sum_output


print(sum_only_int_float([1, 2, 'car', 5.5, 3, 'obj', [1, 2, 3]]))
