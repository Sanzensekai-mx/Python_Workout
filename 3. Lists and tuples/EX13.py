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


def format_sort_records_named_tuple(records):
    parts_of_records = collections.namedtuple('parts_of_records', 'first last time')
    el_records = []
    for el in sorted(records, key=operator.itemgetter(1, 0)):
        el_records.append(parts_of_records(first=el[0], last=el[1], time=el[2]))
    output = []
    for person in el_records:
        output.append(f'{person.last:10} {person.first:10} {person.time:5.2f}')
    print('\n'.join(output))


format_sort_records_named_tuple(PEOPLE)
