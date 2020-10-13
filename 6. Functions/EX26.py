import operator


def calc(string_to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, first, second = string_to_solve.split()
    first, second = int(first), int(second)
    return operations[op](first, second)


# print(calc('+ 1 2'))
# print(calc('- 1 2'))
# print(calc('* 2 2'))


#  EX26_1


def more_num_calc(string_to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    string_to_solve_to_list = string_to_solve.split()
    op, args = string_to_solve_to_list[0], string_to_solve_to_list[1:]
    args = [int(i) for i in args]
    result = 0
    for num in args:
        if args.index(num) == 0:
            result = num
            continue
        result = operations[op](result, num)
    return result


print(more_num_calc('+ 3 5 7'))
print(more_num_calc('/ 100 5 5'))
