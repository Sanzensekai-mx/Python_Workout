import random


def password_generator(str_passwd_symbols):
    def create_passwd(length):
        output = []
        for sym in range(length):
            output.append(random.choice(str_passwd_symbols))
        return ''.join(output)

    return create_passwd


alpha_password = password_generator('abcdef')
symbol_password = password_generator('!@#$%')
print(alpha_password(5))
print(alpha_password(10))
print(symbol_password(5))
print(symbol_password(10))
