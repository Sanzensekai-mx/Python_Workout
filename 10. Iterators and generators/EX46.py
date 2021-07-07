class LoudIterator:
    def __init__(self, data):
        print('\tNow in __init__')
        self.data = data
        self.index = 0

    def __iter__(self):
        print('\tNow in __iter__')
        return self

    def __next__(self):
        print('\tNow in __next__')
        if self.index >= len(self.data):
            print(
                f'\tself.index ({self.index}) is too big; exiting')
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        print(f'\tGot value {value}, incremented index to {self.index}')
        return value


# for one_item in LoudIterator('abc'):
# print(one_item)


def foo():
    yield 1
    yield 2
    yield 3


# print([x for x in foo()])


class MyEnumerate:
    def __init__(self, data, start_index=0):
        self.data = data
        self.start_index = start_index
        self.index = 0

    def __iter__(self):
        return MyEnumerate(self.data, self.start_index)
        # return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index + self.start_index, self.data[self.index])
        # print(f'**** {value}')
        self.index += 1
        return value


for idx, v in MyEnumerate('abcdefg', 1):
    print(f'{idx} - {v}')


# x = MyEnumerate('heghlslsdgjk')
#
# print('***A***')
# for i, v in x:
#     print(f'{i} - {v}')
#
# print('***B***')
# for i, v in x:
#     print(f'{i} - {v}')

def my_enumerate(data, start_index=0):
    index = 0
    for d in data:
        value = (index + start_index, d)
        index += 1
        yield value


for i, v in my_enumerate('abcdefg', 1):
    print(f'{i} - {v}')