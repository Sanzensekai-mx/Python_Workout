import re
import os


pattern = re.compile(r'[\d]+\.[\d]+\.[\d]+\.[\d]+')

all_ip = []
# with open('/var/log/apache2/access.log', 'r') as log:
with open('/var/log/apache2/access.log', 'r') as log:
    for line in log:
        match = re.match(pattern, line)  # Возвращает объект, проверяет на совпадение первый элемент строки
        all_ip.append(match.group())
        # match = re.findall(pattern, line)  # Это если надо вернуть список из всех подходящих
        # for i in match:
        #     all_ip.append(i)


print(set(all_ip))
