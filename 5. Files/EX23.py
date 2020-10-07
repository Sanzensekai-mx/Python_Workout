import json
import glob
import csv


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


csv_passwd_to_json_dict('output_ex22_1_ex23_1.csv', 'output_ex23_2')
