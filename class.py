class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.__price = price  
    
    def say_something(self):
        return "Hello!"
    
    
    def get_price(self):
        return self.__price

class BookStore(Book):
    def get_book_info(self):
        # 
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Price: {self.get_price()}"
    
    def say_something(self):
        return "Where can I find the book store?"


book1 = Book("Python Basics", "John Doe", 2020, 29.99)
bookstore1 = BookStore("The Alchemist", "Paulo Coelho", 1988, 10.99)

# Demonstrate polymorphism
for book in [book1, bookstore1]:
    print(book.say_something())

# Show book info
print(bookstore1.get_book_info())