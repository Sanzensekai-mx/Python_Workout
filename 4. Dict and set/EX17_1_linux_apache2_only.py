import re
import os


pattern = re.compile(r'[\d]+\.[\d]+\.[\d]+\.[\d]+')

all_ip = []
with open('/var/log/apache2/access.log', 'r') as log:
    for line in log:
        match = re.search(pattern, line)
        all_ip.append(match.group(0))

print(set(all_ip))
