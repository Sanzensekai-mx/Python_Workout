import os


def read_all_lines(path_to_dir):
    for num_file, file in enumerate(os.listdir(path_to_dir), 1):
        with open(os.path.join(path_to_dir, file), 'r', encoding='utf-8') as r:
            try:
                for num_line, line in enumerate(r, 1):
                    yield file, num_file, num_line, line
            except OSError:
                pass


for one_line in read_all_lines('C:\\Users\\SanZenSekai\\Desktop\\dir'):
    print(one_line)
