# class Cage:
#     def __init__(self, id_cage):
#         self.id_cage = id_cage
#         self.animals = []
#
#     def add_animals(self, *args):
#         self.animals += args
#
#     def __repr__(self):
#         return f'ID - {self.id_cage}, Animals - {self.animals}'


class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'({self.color} {self.species}, {self.number_of_legs} legs)'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)


# EX43_1 and 43_2

class Wolf(Animal):
    space_required = 2

    def __init__(self, color):
        super().__init__(color, 4)


class Sheep(Animal):
    space_required = 3

    def __init__(self, color):
        super().__init__(color, 4)


class Snake(Animal):
    space_required = 0.5

    def __init__(self, color):
        super().__init__(color, 0)


class Parrot(Animal):
    space_required = 0.5

    def __init__(self, color):
        super().__init__(color, 2)


class Cage:
    animal_dict = {'Sheep': ['Sheep', 'Parrot'], 'Snake': ['Snake', 'Wolf'], 'Parrot': ['Parrot', 'Sheep'],
                   'Wolf': ['Wolf', 'Snake']}

    def __init__(self, id_cage):
        self.id_cage = id_cage
        self.space = 3
        self.animals = []
        self.animals_class = []

    def add_animals(self, *args):
        for idx, i in enumerate(args):
            i_name = i.__class__.__name__
            if len(self.animals) != 0:
                for el in set(self.animals_class):
                    if i_name in self.animal_dict[el]:
                        if i.space_required <= self.space:
                            self.space -= i.space_required
                            self.animals.append(i)
                            self.animals_class.append(i.__class__.__name__)
            else:
                if i.space_required <= self.space:
                    self.space -= i.space_required
                    self.animals.append(i)
                    self.animals_class.append(i.__class__.__name__)

    def __repr__(self):
        return f'ID - {self.id_cage}, Animals - {self.animals}'


class BigCage(Cage):
    def __init__(self, id_cage):
        super().__init__(id_cage)
        # self.animals = []
        self.space = 6


wolf = Wolf('Black')
wolf1 = Wolf('White')
sheep = Sheep('white')
sheep1 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')
parrot1 = Parrot('green')
parrot2 = Parrot('green')

c1 = Cage(1)
c1.add_animals(wolf, sheep)
c2 = Cage(2)
c2.add_animals(snake, parrot, parrot1, snake)
c3 = BigCage(3)
c3.add_animals(wolf, sheep, parrot2, snake, sheep1)
c4 = BigCage(4)
c4.add_animals(sheep, parrot2, wolf1)

print(c1)
print(c2)
print(c3)
print(c4)

# EX43_3
