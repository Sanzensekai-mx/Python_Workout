import json
import glob
import csv
import pathlib
import os
import arrow


def print_scores(dir_name):
    scores = {}
    for filename in glob.glob(f'{dir_name}/*.json'):
        scores[filename] = {}
        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))
            print(subject)
            print(f'''
\tmin {min_score}
\tmax {max_score}
\taverage {average_score}
            ''')


# print_scores('scores')


#  EX23_1


def csv_passwd_to_json(passwd_style_file, name_output_file_json):
    with open(passwd_style_file, 'r', encoding='utf-8') as csv_file, \
            open(f'{name_output_file_json}.json', 'w', encoding='utf-8') as json_file:
        csv_file = csv.reader(csv_file, delimiter='\t')
        list_result = []
        for line in csv_file:
            if len(line) > 1:
                list_result.append(line)
        print(list_result)
        json.dump(list_result, json_file, indent=4)


# csv_passwd_to_json('output_ex22_1_ex23_1.csv', 'output_ex23_1')


#  EX23_2


def csv_passwd_to_json_dict(passwd_style_file, name_output_file_json):
    with open(passwd_style_file, 'r', encoding='utf-8') as csv_file, \
            open(f'{name_output_file_json}.json', 'w', encoding='utf-8') as json_file:
        csv_file = csv.reader(csv_file, delimiter='\t')
        result_list_of_dicts = []
        for line in csv_file:
            if len(line) > 1:
                line_dict = {"name": line[0], "id": line[1], "id_group": line[2], "data": line[3],
                             "home dir": line[4], "shell": line[5]}
                result_list_of_dicts.append(line_dict)
        print(result_list_of_dicts)
        json.dump(result_list_of_dicts, json_file, indent=4)


# csv_passwd_to_json_dict('output_ex22_1_ex23_1.csv', 'output_ex23_2')


#  EX23_3


def json_data_file_in_dir():
    start_path = pathlib.Path.cwd()
    dir_name_or_path = input('Enter the name of dir in current directory or path to dir: ')
    path = pathlib.Path(dir_name_or_path) if '/\\' in dir_name_or_path else pathlib.Path.cwd() / dir_name_or_path
    dict_to_json = {}
    os.chdir(path)
    for file in os.listdir(path):
        if os.path.isfile(pathlib.Path(path) / file):
            dict_to_json[file] = {'size': os.stat(file).st_size,
                                  'last recent mtime': os.stat(file).st_mtime,
                                  'last recent human read': arrow.get(os.stat(file).st_mtime).shift(hours=+4).format(
                                      "YYYY-MM-DD HH:mm:ss")}
    os.chdir(start_path)
    with open('files_data_in_dir.json', 'w', encoding='utf-8') as json_file:
        json.dump(dict_to_json, json_file, indent=4)


def print_data_from_json(json_filename):
    with open(json_filename, 'r', encoding='utf-8') as read_json:
        file_sizes, file_mtime, file_htime  = {}, {}, {}
        for file, dict_values in json.load(read_json).items():
            file_sizes[file] = dict_values['size']
            file_mtime[file] = dict_values['last recent mtime']
            file_htime[file] = dict_values['last recent human read']
        most_recently = max(file_mtime.values())
        least_recently = min(file_mtime.values())
        largest_file_size = max(file_sizes.values())
        smallest_file_size = min(file_sizes.values())
        for k, v in file_sizes.items():
            if v == largest_file_size:
                largest_file = k
            if v == smallest_file_size:
                smallest_file = k
        for k, v in file_mtime.items():
            if v == most_recently:
                most_recently_file = k
            if v == least_recently:
                least_recently_file = k
    # print(file_sizes)
    # print(file_mtime)
    print(f"""
Modified most recently "{most_recently_file}"  -  {file_htime[most_recently_file]}
Modified least recently "{least_recently_file}"  -  {file_htime[least_recently_file]}
Largest file "{largest_file}"  -  size: {largest_file_size}
Smallest file "{smallest_file}"  -  size: {smallest_file_size}
""")


json_data_file_in_dir()
print_data_from_json('files_data_in_dir.json')

#  for tests func json_data_file_in_dir()
#  C:\Users\Sanzensekai\PycharmProjects\Python_Workout\5. Files
#  dir_for_EX20_3
