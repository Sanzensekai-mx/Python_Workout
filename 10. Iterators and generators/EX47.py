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


c = Circle('abc', 5)
print(list(c))


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


print('*************')
c = Circle('abc', 5)
print(list(c))
