import os


def read_all_lines(path_to_dir):
    for num_file, file in enumerate(os.listdir(path_to_dir), 1):
        with open(os.path.join(path_to_dir, file), 'r', encoding='utf-8') as r:
            try:
                for num_line, line in enumerate(r, 1):
                    yield file, num_file, num_line, line
            except OSError:
                pass


# for one_line in read_all_lines('C:\\Users\\SanZenSekai\\Desktop\\dir'):
#     print(one_line)


def read_all_lines_v2(path_to_dir):
    idx = 0
    l = 1
    max_line_files = []
    for num_file, file in enumerate(os.listdir(path_to_dir), 1):
        path = os.path.join(path_to_dir, file)
        with open(path, 'r', encoding='utf-8') as r:
            max_line_files.append(len(r.readlines()))
    while l <= max(max_line_files):
        for num_file, file in enumerate(os.listdir(path_to_dir), 1):
            path = os.path.join(path_to_dir, file)
            with open(path, 'r', encoding='utf-8') as r:
                try:
                    # for num_line, line in enumerate(r, 1):
                    #     yield file, num_file, num_line, line
                    j = r.readlines()
                    # print(j[idx])
                    yield file, num_file, l, j[idx]
                except OSError:
                    pass
                except IndexError:
                    pass
        idx += 1
        l += 1


for one_line in read_all_lines_v2('C:\\Users\\SanZenSekai\\Desktop\\dir'):
    print(one_line)
