import os


def read_all_lines(path_to_dir):
    for file in os.listdir(path_to_dir):
        with open(os.path.join(path_to_dir, file), 'r', encoding='utf-8') as r:
            try:
                for line in r:
                    yield line
            except OSError:
                pass


for one_line in read_all_lines('C:\\Users\\SanZenSekai\\Desktop\\dir'):
    print(one_line)
