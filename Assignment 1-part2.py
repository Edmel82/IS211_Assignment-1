class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        return f"{self.title}, written by {self.author}"

# Instantiate two books
harry_potter = Book(author="J. K. Rowling", title="Harry Potter and the Goblet of Fire")
ivanhoe = Book(author="Walter Scott", title="Ivanhoe: A Romance")

# Print their details
print(harry_potter.display())
print(ivanhoe.display())
