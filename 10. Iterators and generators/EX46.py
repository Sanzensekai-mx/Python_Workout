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
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return MyEnumerate(self.data)

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index])
        self.index += 1
        return value


for idx, v in MyEnumerate('abcdefg'):
    print(f'{idx} - {v}')
