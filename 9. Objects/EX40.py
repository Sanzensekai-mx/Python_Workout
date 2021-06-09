class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []
        # self..max_scoops = 3

    def add_scoops(self, *new_snoops):
        for one_snoop in new_snoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_snoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)

# print(b)


# EX40_1 EX40_2
class Person:
    population = 0

    def __init__(self):
        Person.population += 1

    def __del__(self):
        Person.population -= 1


p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

# print(Person.population)

del p1
del p2
del p3
del p4
del p5


# print(Person.population)
# print(p1.population)

# EX40_3


class Transaction:
    total_sum = 0

    def deposit(self, value):
        self.total_sum += value

    def withdrawal(self, value):
        self.total_sum -= value


t = Transaction()
t.deposit(1000)
t.withdrawal(500)
print(t.total_sum)
t.withdrawal(600)
print(t.total_sum)
t.deposit(200)
print(t.total_sum)
