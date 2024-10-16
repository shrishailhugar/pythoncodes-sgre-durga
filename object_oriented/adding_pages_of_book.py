class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def __add__(self, other):
        # return self.pages+other.pages
        # print(self.pages+other.pages)
        return Book(self.name + other.name, self.pages + other.pages)

    def __mul__(self, other):
        return Book(self.name + other.name, self.pages * other.pages)

    def __str__(self):
        return f'the pages are {self.name, self.pages}'


b1 = Book('a', 100)
b2 = Book('b', 200)
b3 = Book('c', 400)
b4 = Book('d', 5)
print(b1 + b2 + b3)
print(b1 + b2 * b4 + b3)
