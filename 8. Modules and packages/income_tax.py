def calculate_income_tax(salary):
    if salary <= 1000:
        salary_with_tax = salary
    else:
        tax_brackets = [1000]
        i = 0
        for x in range(1, salary - 999):
            if len(tax_brackets) == 3:
                remains = salary - 21000
                tax_brackets.append(remains)
                break
            else:
                if i == 10000:
                    tax_brackets.append(i)
                    i -= 10000
            i += 1
        else:
            tax_brackets.append(i)
        for bracket in range(1, len(tax_brackets)):
            arg = [0, 0.9, 0.8, 0.5]
            tax_brackets[bracket] *= arg[bracket]
        salary_with_tax = sum(tax_brackets)
    return f'Ваша зарплата c учётом налога: {salary_with_tax}'
