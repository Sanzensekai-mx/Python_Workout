# В следующем примере пароли будут хешироваться для последующего сохранения в базе данных.
# Здесь мы будем использовать salt. salt является случайной последовательностью, добавленной к строке пароля
# перед использованием хеш-функции. salt используется для предотвращения перебора по словарю (dictionary attack)
# и атак радужной таблицы (rainbow tables attacks).
# Тем не менее, если вы занимаетесь реально функционирующим приложением и работаете над паролями пользователей,
# следите за последними зафиксированными уязвимостями в данной области.
import uuid
import hashlib


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


new_pass = input('Введите пароль: ')
hashed_password = hash_password(new_pass)
print('Строка для хранения в базе данных: ' + hashed_password)
old_pass = input('Введите пароль еще раз для проверки: ')

if check_password(hashed_password, old_pass):
    print('Вы ввели правильный пароль')
else:
    print('Извините, но пароли не совпадают')