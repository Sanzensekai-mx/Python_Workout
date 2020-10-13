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
