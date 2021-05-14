from typing import List
from dataclasses import dataclass, field


@dataclass
class Scoop:
    flavor: str


@dataclass
class Bowl:
    scoops: List[Scoop] = field(default_factory=list)

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)

print(b)


# Наследование
class Foo():
    def __init__(self, x):
        self.x = x

    def x2(self):
        return self.x * 2


class Bar(Foo):
    def x3(self):
        return self.x * 3


b = Bar(10)

print(b.x2())
print(b.x3())
