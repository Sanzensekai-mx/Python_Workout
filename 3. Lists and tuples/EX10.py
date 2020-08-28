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
            output += item
    return output


print(bigger_than(10, 5, 20, 30, 6))
