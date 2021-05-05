def true_char_dict(string):
    result_dict = {'isdigit': 0, 'isalpha': 0, 'isspace': 0}
    for char in string:
        if char.isdigit():
            result_dict['isdigit'] += 1
        elif char.isalpha():
            result_dict['isalpha'] += 1
        elif char.isspace():
            result_dict['isspace'] += 1
    return result_dict
