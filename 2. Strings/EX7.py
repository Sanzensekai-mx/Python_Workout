def ubbi_dubbi(str):
    output = []
    for char in str:
        if char in 'aeiouAEIOU':
            output.append(f'ub{char}') if str[0] != char else output.append(f'Ub{char.lower()}')
        else:
            output.append(char)
    return ''.join(output)


# print(ubbi_dubbi('Milk'))
# print(ubbi_dubbi('Program'))
# print(ubbi_dubbi('Octopus'))


def delete_name(article, list_names):
    article_list = article.split()
    for word in article_list:
        if word in list_names:
            article_list[article_list.index(word)] = '_'
    return ' '.join(article_list)


names = ['Алексей', 'Навальный', 'Гоша']
a = '''
По мнению немецких врачей, результаты обследования блогера Алексей Навальный указывают на интоксикацию веществом из 
группы ингибиторов холинэстеразы. При этом конкретное вещество пока Алексей Навальный неизвестно, проводятся исследования. Об этом 
говорится в понедельник, 24 августа, в заявлении немецкой клиники «Шарите» в Германии, где Алексей находится на лечении .
'''
# print(delete_name(a, names))

import re


def url_encode(string):
    pattern = r'\W'
    for char in string:
        if char in re.findall(pattern, string):
            char_a = f'%{hex(ord(char))[2:].upper()}'
            return string.replace(char, char_a)


print(url_encode('11..22 33'))