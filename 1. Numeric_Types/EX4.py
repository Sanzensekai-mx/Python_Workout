def hex_output():
    hex_num = input('Enter hex number to convert: ')
    dec_num = 0
    for power, digit in enumerate(reversed(hex_num)):
        dec_num += int(digit, 16) * (16 ** power)
    print(dec_num)


hex_output()


def hex_output2():
    hex_num = input('Enter hex number to convert: ')
    dec_num = 0
    dict_chr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dict_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for power, digit in enumerate(reversed(hex_num)):
        if 70 >= ord(digit) >= 65:
            dec_num += dict_chr[digit] * (16 ** power)
        else:
            dec_num += dict_num[digit] * (16 ** power)
    print(dec_num)


# hex_output2()


def name_triangle(name):
    i = 0
    for c in range(len(name)):
        if c == 0:
            print(name[i:c+1])
            continue
        print(name[i:c+1])


# name_triangle('Ivan')
