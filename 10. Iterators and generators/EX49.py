import time
import os
import datetime


def iter_counter(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield delta, item


# for i in iter_counter('abcdefg'):
#     print(i)
#     time.sleep(2)


# 1
def iter_counter_v2(data, min_time):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        if delta < min_time:
            time.sleep(min_time - delta)
        last_time = time.perf_counter()
        yield delta, item


# for i in iter_counter_v2('abcdefg', 10):
#     print(i)


# 2

def file_usage_timing(path_dir):
    for file in os.listdir(path_dir):
        file_info = os.stat(os.path.join(path_dir, file))
        yield file, datetime.datetime.fromtimestamp(file_info.st_atime), datetime.datetime.fromtimestamp(
            file_info.st_mtime), datetime.datetime.fromtimestamp(file_info.st_ctime)


# for f in file_usage_timing('C:\\Users\\SanZenSekai\\Desktop\\dir'):
#     print(f)


# 3

def iter_with_filter(data, func):
    for d in data:
        if func(d):
            yield d


for i in iter_with_filter([1, 3, 214, 43, 2, 13, 54, 57], lambda x: x > 10):
    print(i)
