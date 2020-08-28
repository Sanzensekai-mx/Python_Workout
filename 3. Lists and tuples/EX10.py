def my_sum(*args):
    if not args:
        return ()
    output = args[0]
    for item in args[1:]:
        output += item
    return output


# print(my_sum('abc', 'def'))
# print(my_sum([1, 2, 3], [4, 5, 6]))
# print(my_sum(1, 2, 3))
# print(my_sum())


def bigger_than(first_elem, *args):
    if not first_elem and args:
        return ()
    output = args[0]
    for item in args:
        if item < first_elem:
            if item == output:
                output -= item
            continue
        else:
            if output != item:
                output += item
            else:
                continue
    return output


# print(bigger_than(10, 5, 20, 30, 6))
# print(bigger_than(11, 10, 25, 26, 1))
# print(bigger_than('abc', 'def', 'adads'))


def sum_numeric(*args):
    total = 0
    for item in args:
        try:
            total += int(item)
        except Exception as e:
            continue
    return total


print(sum_numeric(10, 20, 'a', '30', 'bcd'))
print(sum_numeric(50, 80.5, '30', [1, 2, 3]))


def sum_dict(list_of_dicts):
    result_dict = {}
    all_keys = [el for key in list_of_dicts for el in key]
    not_all_keys = []
    for dict_l in list_of_dicts:
        for k, v in dict_l.items():
            if all_keys.count(k) > 1 and not_all_keys.count(k) == 0:
                result_dict[k] = [v]
                not_all_keys.append(k)
                continue
            elif not_all_keys.count(k) != 0:
                result_dict[k].append(v)
                not_all_keys.append(k)
                continue
            else:
                result_dict[k] = v
                not_all_keys.append(k)
    # print(not_all_keys)
    # print(all_keys)
    return result_dict


print(sum_dict([{'A': 11, 'B': 12, 'C': '15', 'a': 3}, {'a': 2, 'b': 1, 'c': '5'}, {'a': 2, 'b': 3}, {'a': 5}]))
print(sum_dict([{'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2}]))
