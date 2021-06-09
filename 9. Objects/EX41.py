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


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')
s4 = Scoop('flavor 4')
s5 = Scoop('flavor 5')

b = Bowl()
bb = BigBowl()

b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)

bb.add_scoops(s1, s2)
bb.add_scoops(s3)
bb.add_scoops(s4, s5)


# print(b)
# print('====')
# print(bb)

# EX41_1
# Переменные экземпляра класса предназначены для данных, уникальных для каждого экземпляра класса,
# а переменные класса (атрибуты данных класса) - для атрибутов и методов, общих для всех экземпляров класса.


class Envelope:
    def __init__(self, weight):
        self.weight = weight
        self.was_sent = False
        self.postage = 0

    def send(self):
        if self.postage_needed() <= self.postage:
            print('Письмо отправлено')
            self.was_sent = True
        else:
            print('Письмо не отправлено. Недостаточно почтовой оплаты.')

    def add_postage(self, postage):
        self.postage += postage

    def postage_needed(self):
        return self.weight * 10


class BigEnvelope(Envelope):
    def postage_needed(self):
        return self.weight * 15


e = Envelope(100)
be = BigEnvelope(1000)
# print(be.postage_needed())
# be.send()
be.add_postage(13000)
# print(be.weight, be.was_sent, be.postage)
be.add_postage(2000)
# be.send()
# print(be.weight, be.was_sent, be.postage)
# e.send()
# e.add_postage(1000)
# e.send()
# print(e.postage_needed())
# print(e.weight, e.was_sent, e.postage)


# EX41_2

class Phone:
    @staticmethod
    def dial():
        return 'Набор номера 8927832**** ...'


class SmartPhone(Phone):
    def run_app(self):
        print(f'{self.dial()}, но через приложение.')


class IPhone(SmartPhone):
    def dial(self):
        return f'{super().dial().lower()} с iphone'


# p = Phone()
# print(p.dial())
#
# sp = SmartPhone()
# sp.run_app()
#
# ip = IPhone()
# print(ip.dial())
# ip.run_app()

# EX41_3

class Bread:
    calories = 201
    carbohydrates = 15.08
    sodium = 400
    fat = 1.40

    def get_nutrition(self, num_of_slices):
        return {'calories': self.calories * num_of_slices,
                'carbohydrates': self.carbohydrates * num_of_slices,
                'sodium': self.sodium * num_of_slices,
                'fat': self.fat * num_of_slices}


class WhiteBread(Bread):
    calories = 250
    carbohydrates = 18.21
    sodium = 420
    fat = 3.32


b = Bread()
print(b.get_nutrition(2))
wb = WhiteBread()
print(wb.get_nutrition(2))
