#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run only on linux
import pprint


# main ex


def passwd_to_dict(passwd_file):
    users = {}
    with open(passwd_file, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                users[user_info[0]] = int(user_info[2])
    return users


# print(passwd_to_dict('/etc/passwd'))

# ex 19_1

def passwd_to_dict_2(passwd_file):
    login_shells_users = {}
    with open(passwd_file, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                info = list(map(lambda x: x.strip('\n'), line.split(':')))
                if info[-1] in login_shells_users.keys():
                    login_shells_users[info[-1]] = [i for i in login_shells_users[info[-1]]] + [info[0]] \
                        if type(login_shells_users[info[-1]]) == list \
                        else [login_shells_users.get(info[-1])] + [info[0]]
                    continue
                login_shells_users[info[-1]] = info[0]
    return login_shells_users


# pprint.pprint(passwd_to_dict_2('/etc/passwd'))


def enter_int_to_dict():
    result = {}
    print('Enter integers, separated by spaces')
    user_input = input('--> ').strip()
    split_str = [int(i) for i in user_input.split()]
    for num in split_str:
        result[num] = [int(num / i) for i in split_str if num % i == 0]
    return result


print(enter_int_to_dict())
