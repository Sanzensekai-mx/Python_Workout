from fredonia import calculate_tax
from income_tax import calculate_income_tax
from true_characters import true_char_dict
from another_fromkeys import new_dict

tax_at_12noon = calculate_tax(100, 'Harpo', 12)
tax_at_9pm = calculate_tax(100, 'Harpo', 21)

# print(f'You owe a total of: {tax_at_12noon}')
# print(f'You owe a total of: {tax_at_9pm}')
# print(calculate_tax(100, 'Zeppo', 12))

# Ex 36a
print(calculate_income_tax(16000))

# Ex 36b
print(true_char_dict('Это прексрасный 27-ой день апреля.'))

# Ex 36c
print(new_dict.another_fromkeys('abc1', id))
