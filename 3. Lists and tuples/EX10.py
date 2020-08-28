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

