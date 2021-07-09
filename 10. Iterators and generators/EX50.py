from itertools import chain
import os


# for one_item in chain('abc', [1, 2, 3]):
#     print(one_item)

def my_chain(*args):
    for item in args:
        for i in item:
            yield i


# for one_item in my_chain('abc', [1, 2, 3]):
#     print(one_item)

# 1

def my_zip(*args):
    for a in range(len(min(args, key=len))):
        yield tuple(one[a] for one in args)


# for one_item in my_zip('abc', [1, 2, 3]):
#     print(one_item)

# 2

def read_all_lines(path_to_dir):
    # for filename in os.listdir(path_to_dir):
    #     if os.path.isfile(os.path.join(path_to_dir, filename)):
    #         with open(os.path.join(path_to_dir, filename), 'r', encoding='utf-8') as r:
    #             return my_chain(r)
    return my_chain(*(open(os.path.join(path_to_dir, filename), 'r', encoding='utf-8') for filename in os.listdir(path_to_dir) if
                      os.path.isfile(os.path.join(path_to_dir, filename))))


for one_line in read_all_lines('C:\\Users\\SanZenSekai\\Desktop\\dir'):
    print(one_line)
