import json
import glob


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


print_scores('scores')
