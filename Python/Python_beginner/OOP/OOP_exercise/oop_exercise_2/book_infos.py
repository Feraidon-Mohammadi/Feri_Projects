"""
Exercise 2: Create a Book Class
Create a Book class with attributes title, author, and published_year.
Implement a method called display_info that prints information about the book.
"""

class Book1:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def display_info(self):
        data = f"book Info's \n\ntitle: {self.title}\nAuthor: {self.author}\nPublished_year: {self.published_year}"
        print(data)


d1 = Book1("History", "Roy Anderson", "1994-09-23")
d1.display_info()

d2 = Book1("Documentary", "Megan Rapid", "1933-01-01")
d2.display_info()


#################################### or ########################################################

class Book2:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def display_info(self):
        data = f"book Info's \n\ntitle: {self.title}\nAuthor: {self.author}\nPublished_year: {self.published_year}"
        return data


x = Book2("History", "Roy Anderson", "1994-09-23")
f1 = x.display_info()

x = Book2("Documentary", "Megan Rapid", "1933-01-01")
f2 =x.display_info()
print(f1)
print(f2)

# +++++++++++++ here i can add them in to a list +++++++++++++++#

my_list = []
my_list.append(x.title)
my_list.append(x.author)
my_list.append(x.published_year)
my_list.append(d1.author)

print(f"listed data: {my_list}")
