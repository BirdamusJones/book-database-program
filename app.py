from models import (Base, session, Book, engine)
import csv

# import models
# main menu - add, search, analysis, exit, view - class?
# def add_books():
#     book_ls = []
#     with open('suggested_books.csv', newline= '') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             book_ls.append()
#         for i in book_ls:




        
        
    # add books to the database - function
# def edit_books():
# edit books - function

# def delete_books(self):
#     self.title = input('What is the title of the book you would like to delete?\n')
#     if self.title = models.
# return models.session.delet(book)

# def search_books():
# # search books - function

# def clean_data():
# # data cleaning - function
# # loop runs program

if __name__ == '__main__':
    Base.metadata.create_all(engine)



# def add_books(self):
#     self.title = input('What is the title of the book?\n')
#     self.author = input('Who is the author?\n')
#     self.date_published = input('What date was it published?\n')
#     self.price = input('What will it cost?\n')
#     new_book = models.Book(title='{self.title}',author='{self.author}',date_published='{self.date_published}',price='{self.price}')
# return models.session.add(new_book)