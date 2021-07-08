class CircleIterator:
    def __init__(self, sequence, num):
        self.num = num
        self.sequence = sequence
        self.index = 0

    def __next__(self):
        if self.index >= self.num:
            raise StopIteration
        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value


class Circle:
    def __init__(self, num, sequence):
        self.num = num
        self.sequence = sequence

    def __iter__(self):
        return CircleIterator(self.num, self.sequence)


# c = Circle('abc', 5)
# print(list(c))


class Circle:
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times

    def __iter__(self):
        n = len(self.data)
        return (self.data[x % n] for x in range(self.max_times))


# 1

class Circle(CircleIterator):
    def __init__(self, sequence, num):
        super().__init__(sequence, num)
        # self.returns =

    def __iter__(self):
        return Circle(self.sequence, self.num)


# print('*************')
# c = Circle('abc', 5)
# print(list(c))


# 2

def circle(sequence, num):
    return (sequence[x % len(sequence)] for x in range(num))


# print('*************')
# print(list(circle('abc', 5)))


# 3

class MyRangeIterator:
    def __init__(self, start: int, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop
        self.step = step

    def __next__(self):
        while self.start < self.stop:
            value = self.start
            self.start += self.step
            return value
        else:
            raise StopIteration


class MyRange(MyRangeIterator):
    def __init__(self, start: int, stop=None, step=1):
        super().__init__(start, stop, step)

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)


for i in MyRange(5, 10, 2):
    print(i)
