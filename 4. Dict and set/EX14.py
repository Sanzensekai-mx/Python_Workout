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


check_user_pass()



