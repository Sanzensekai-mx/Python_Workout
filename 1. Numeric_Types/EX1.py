import random


def guessing_game():
    secret_number = random.randint(0, 100)
    print('Загадано число от 0 до 100')
    i = 0
    while i < 5:
        player_input = int(input('Введите число: '))
        if player_input > secret_number:
            print(f'Your number {player_input} is too high')
            i += 1
        elif player_input < secret_number:
            print(f'Your number {player_input} is too low')
            i += 1
        else:
            print(f'Just right, the secret number is {player_input}')
            break


guessing_game()
