class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_snoops):
        for one_snoop in new_snoops:
            self.scoops.append(one_snoop)
        # for f in [scoop.flavor for scoop in args]:
        #     self.scoops.append(f)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)


# print(b)


# EX39_1

class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


# EX39_3
class Shelf:
    def __init__(self):
        self.books = []
        # EX39_3
        self.width_limit = 45
        self.total_width = 0

    def add_book(self, *new_books):
        for one_book in new_books:
            self.books.append(one_book)
        # EX39_3
            self.total_width += one_book.width
        if self.total_width > self.width_limit:
            raise ShelfWidthError

    def total_price(self):
        return f'Общая сумма книг на полке: {sum(b.price for b in self.books)} рублей'

    # EX39_2
    def has_book(self, book_title):
        if book_title in (book.title for book in self.books):
            return True
        return False

    def __repr__(self):
        return '\n'.join(s.title for s in self.books)


# EX39_3
class ShelfWidthError(Exception):
    print('Слишком много книг на полке')


b1 = Book(title='Грокаем алгоритмы', author='Адитья Бхаргава', price=500, width=15)
b2 = Book(title='7 навыков высокоэффективных людей', author='Стиван Р. Кови', price=1000, width=25)
b3 = Book(title='Государство и революция', author='В. И. Ленин', price=150, width=7)

s = Shelf()
s.add_book(b1, b2)
s.add_book(b3)
print(s)
print(s.total_price())
print(s.has_book('Ван пис'))
print(s.has_book('Государство и революция'))
