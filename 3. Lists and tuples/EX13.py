import operator
import collections


def format_sort_records(records):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'
    for person in sorted(records, key=operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    print('\n'.join(output))


PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


# format_sort_records(PEOPLE)


