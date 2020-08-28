def my_sum(*args):
    if not args:
        return ()
    output = args[0]
    for item in args[1:]:
        output += item
    return output


print(my_sum('abc', 'def'))
print(my_sum([1, 2, 3], [4, 5, 6]))
print(my_sum(1, 2, 3))
