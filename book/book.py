class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price 

    def info(self):
        return f"'{self.title}' by {self.author}, Price: ${self.__price}"

    def read_sample(self):
        return "Physical book sample"


class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size

    def read_sample(self):
        return "Digital sample of the eBook."


book1 = Book("30", "Hamilton P", 25)
ebook1 = EBook("Burnt Bridges", "Leon Polo", 5, "10MB")

print(book1.info())
print(book1.read_sample())

print(ebook1.info())
print(ebook1.read_sample())
