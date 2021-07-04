class NotCageObjectException(Exception):
    pass


class NoPlaceCage(Exception):
    pass


class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        for el in args:
            try:
                if el.__class__.__name__ != 'Cage' or 'BigCage':
                    self.cages.append(el)
                else:
                    raise NotCageObjectException
            except NotCageObjectException:
                print('В метод переданы объекты не принадлежащие классу Cage')

    def transfer_animal(self, transfer_animal, target_zoo):
        for cage in self.cages.copy():
            for animal in cage.animals.copy():
                if transfer_animal is animal:
                    cage.animals.remove(animal)
                    break
            break
        for cage in target_zoo.cages:
            cage.add_animals(transfer_animal)
            if cage.animals[-1] is transfer_animal:
                break

    def animals_by_color(self, color):
        return [animal for cage in self.cages for animal in cage.animals if animal.color == color]

    def animals_by_legs(self, legs):
        return [animal for cage in self.cages for animal in cage.animals if animal.number_of_legs == legs]

    def number_of_legs(self):
        return sum([animal.number_of_legs for cage in self.cages for animal in cage.animals])

    def __repr__(self):
        # print()
        return '\n'.join(str(cage) for cage in self.cages)


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
            try:
                if len(self.animals) != 0:
                    for el in set(self.animals_class):
                        if i_name in self.animal_dict[el]:
                            if i.space_required <= self.space:
                                self.space -= i.space_required
                                self.animals.append(i)
                                self.animals_class.append(i.__class__.__name__)
                            else:
                                raise NoPlaceCage
                        else:
                            raise NoPlaceCage
                else:
                    if i.space_required <= self.space:
                        self.space -= i.space_required
                        self.animals.append(i)
                        self.animals_class.append(i.__class__.__name__)
            except NoPlaceCage:
                print(f'Зверь {i} не подходит для клетки {self}')

    def __repr__(self):
        return f'ID - {self.id_cage}, Animals - {self.animals}'


class BigCage(Cage):
    def __init__(self, id_cage):
        super().__init__(id_cage)
        # self.animals = []
        self.space = 12


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


z = Zoo()

wolf = Wolf('black')
wolf1 = Wolf('white')
sheep = Sheep('white')
sheep1 = Sheep('white')
snake = Snake('black')
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

z.add_cages(c1, c2, c3, c4)
print(z.cages)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))
print(z.number_of_legs())
print(z)

z2 = Zoo()

c21 = Cage(1)
c21.add_animals(sheep1, parrot)
c22 = Cage(2)
c22.add_animals(sheep)
c23 = BigCage(3)
c23.add_animals(wolf, wolf)

z2.add_cages(c21, c22, c23)

z.transfer_animal(wolf, z2)
print(z)
print(z2)
