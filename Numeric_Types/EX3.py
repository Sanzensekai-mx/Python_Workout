import decimal


def run_timing():
    number_of_runs = 0
    total_time = 0
    while True:
        user_input = input('Enter 10 km run time: ')
        if not user_input:
            break
        else:
            number_of_runs += 1
            total_time += float(user_input)
    return f'Average of {total_time / number_of_runs}, over {number_of_runs} runs'


# print(run_timing())

def func_float(float_num, before, after):
    list_of_float = str(float_num).split('.')
    before_0 = list_of_float[0][-before:]
    after_1 = list_of_float[1][:after]
    new_float = float(f'{before_0}.{after_1}')
    return new_float


# print(func_float(1234.5678, 2, 3))


def func_decimal(num1, num2):
    return decimal.Decimal(num1) + decimal.Decimal(num2)


# print(func_decimal('0.2', '0.1'))
