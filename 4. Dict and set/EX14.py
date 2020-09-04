MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}


def take_order():
    total_prise = 0
    while True:
        user_order = input('Hello. I will take your order: ').strip()
        if not user_order:
            break
        if user_order in MENU:
            total_prise += MENU[user_order]
            print(f'{user_order} costs {MENU[user_order]}, total is {total_prise}')
            continue
        else:
            print(f'Sorry, we are fresh out of {user_order} today.')
            continue
    print(f'Your total is {total_prise}')


# take_order()

user_pass = {'Ivan': 'qwerty', 'Andri': '1234', 'K': 'first'}


def check_user_pass():
    while True:
        username = input('Enter username: ').strip()
        password = input('Enter password: ')
        if username in user_pass.keys() and user_pass[username] == password:
            print('Access received')
            break
        print('Incorrect username or password')


# check_user_pass()


date_temp = {'2.09': '+19', '3.09': '+18', '4.09': '+18', '5.09': '+19', '6.09': '+20'}


def temp_in_date():
    while True:
        user_input = input('Enter the date (example: 1.08, 7.09): ').strip()
        try:
            print(
                f'Date {str(int(user_input[0]) - 1) + user_input[1:]} temp is {date_temp[str(int(user_input[0]) - 1) + user_input[1:]]}')
        except KeyError:
            print('Don\'t have information for yesterday')
        print(f'Date {user_input} temp is {date_temp[user_input]}')
        try:
            print(
                f'Date {str(int(user_input[0]) + 1) + user_input[1:]} temp is {date_temp[str(int(user_input[0]) + 1) + user_input[1:]]}')
        except KeyError:
            print('Don\'t have information for tomorrow')


# temp_in_date()

import datetime

names = {'Ivan': datetime.date(year=2000, month=4, day=27), 'Ilnaz': datetime.date(year=2000, month=4, day=25),
         'Mother': datetime.date(year=1978, month=12, day=8), 'Kris': datetime.date(year=2001, month=2, day=18)}


def how_many_days():
    today = datetime.date.today()
    while True:
        user_input = input('--> ').strip()
        if user_input:
            try:
                period = today - names[user_input]
                print(f'days of life {period.days}')
            except KeyError:
                print('Нет имени в словаре')
        else:
            break


how_many_days()
