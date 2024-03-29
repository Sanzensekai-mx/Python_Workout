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


# print(more_num_calc('+ 3 5 7'))
# print(more_num_calc('/ 100 5 5'))


#  EX26_2


def apply_to_each(func, iterable):
    return list(map(func, iterable))


# print(apply_to_each(chr, [1, 2, 3, 4, 5]))
# print(apply_to_each(lambda x: int(x) + 100, ['1', '2', '3', '4', '5']))


#  EX26_3


def transform_lines(func, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as in_f, open(output_file, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            if line == '\n':
                out_f.write('\n')
            out_f.write(f"{''.join(list(map(func, line.split())))}\n")


transform_lines(lambda x: f' {x} Ivan', 'stix6.txt', 'output_26_3.txt')
