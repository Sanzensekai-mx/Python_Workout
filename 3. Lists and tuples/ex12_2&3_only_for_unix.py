import os
import pprint
import operator


os.chdir('/etc')
result = []
with open('passwd') as p:
    for line in p:
        new_line = line.split(':')
        result.append([new_line[0], new_line[-1][:-1]])

# pprint.pprint(result)

result_of_dicts = []
result_keys = ['Username', 'Shell']
for ls in result:
    result_of_dicts.append(dict(zip(result_keys, ls)))


# pprint.pprint(result_of_dicts)

for l in sorted(result_of_dicts, key=operator.itemgetter('Shell', 'Username'), reverse=True):
    print(f"{l['Username']} -- {l['Shell']}")
print('------------------------------')
for l in sorted(result_of_dicts, key=operator.itemgetter('Username', 'Shell')):
    print(f"{l['Username']} -- {l['Shell']}")
