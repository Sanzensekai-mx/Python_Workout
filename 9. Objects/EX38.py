class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


# scoops = [Scoop(flavor).flavor for flavor in ('chocolate', 'vanilla', 'persimmon')]
# print(scoops)


def create_scoops():
    scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)


create_scoops()


#  EX38_1  EX38_2


class Beverage:
    # EX38_2 Добавлено temperature=75 по умолчанию
    def __init__(self, name, temperature=75):
        self.name = name
        self.temperature = temperature


tea = Beverage(name='Tea', temperature=90)
vodka = Beverage(name='Vodka', temperature=10)
ice_tea = Beverage(name='Ice tea', temperature=0)
wickey = Beverage(name='Wickey')
leto = Beverage(name='Leto')

list_beverage = [tea, vodka, ice_tea, wickey, leto]
for b in list_beverage:
    print(b.name)
    print(b.temperature)
    print()


#  EX38_3


class LogFile:
    def __init__(self, file):
        self.file = open(file, 'w')
        # self.file = file


log_file = LogFile(file='password.txt')
log_file.file.write("It's log file")
log_file.file.close()
