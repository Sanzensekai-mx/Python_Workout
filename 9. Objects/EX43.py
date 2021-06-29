class Animal:
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


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


# wolf = Wolf('Black')
# sheep = Sheep('white')
# snake = Snake('brown')
# parrot = Parrot('green')

# print(wolf)
# print(sheep)
# print(snake)
# print(parrot)


# EX43_1
class Animal:
    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color


class ZeroLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 0

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class TwoLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 2

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class FourLeggedAnimal(Animal):
    def __init__(self, color):
        super().__init__(color)
        self.number_of_legs = 4

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class Wolf(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Snake(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


# wolf = Wolf('Black')
# sheep = Sheep('white')
# snake = Snake('brown')
# parrot = Parrot('green')
#
#
# print(wolf)
# print(sheep)
# print(snake)
# print(parrot)


# EX43_2

class Animal:
    number_of_legs = None

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.color} {self.species}, {self.number_of_legs} legs'


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0


class TwoLeggedAnimal(Animal):
    number_of_legs = 2


class FourLeggedAnimal(Animal):
    number_of_legs = 4


class Wolf(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Sheep(FourLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Snake(ZeroLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    def __init__(self, color):
        super().__init__(color)


# wolf = Wolf('Black')
# sheep = Sheep('white')
# snake = Snake('brown')
# parrot = Parrot('green')
#
# print(wolf)
# print(sheep)
# print(snake)
# print(parrot)


# EX43_3

class Animal:
    number_of_legs = None
    animal_sound = None

    def __init__(self, color):
        self.species = self.__class__.__name__
        self.color = color

    def __repr__(self):
        return f'{self.animal_sound} - {self.color} {self.species}, {self.number_of_legs} legs'


class ZeroLeggedAnimal(Animal):
    number_of_legs = 0


class TwoLeggedAnimal(Animal):
    number_of_legs = 2


class FourLeggedAnimal(Animal):
    number_of_legs = 4


class Wolf(FourLeggedAnimal):
    animal_sound = 'Wuf'

    def __init__(self, color):
        super().__init__(color)


class Sheep(FourLeggedAnimal):
    animal_sound = 'Baa'

    def __init__(self, color):
        super().__init__(color)


class Snake(ZeroLeggedAnimal):
    animal_sound = 'Shhhh'

    def __init__(self, color):
        super().__init__(color)


class Parrot(TwoLeggedAnimal):
    animal_sound = 'Повесить на рее эту сухопутную крысу'

    def __init__(self, color):
        super().__init__(color)


wolf = Wolf('Black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

print(wolf)
print(sheep)
print(snake)
print(parrot)
