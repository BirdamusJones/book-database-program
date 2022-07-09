# import models
from models import (Base, session, Book, engine)
import csv
import datetime


# main menu - add, search, analysis, exit, view - class?
def menu():
    while True:
        print('''
              \nPROGRAMMING BOOKS 
              \r1) Add book
              \r2) View all books
              \r3) Search for book
              \r4) Book Analaysis
              \r5) EXIT''')
        choice = input('What would you like to do?\n')
        if choice in ['1','2','3','4','5']:
            return choice
        else:
            input('''
            \nPlease choose one of the options above.
            \rA number from 1-5
            \rPress enter to try again''')
# add books to the database - function                          
# def add_book():
#     title = input('What is the title of the book?\n')
#     author = input('Who is the author?\n')
#     date_published = input('What date was it published?\n')
#     price = input('What is the cost?\n')
#     new_book = models.Book(title = '{title}', author = '{author}', date_published = '{date_published}', price = '{price}') 
#     return new_book

# def edit_books():
# edit books - function
# def delete_books(self):
# def search_books():
# # search books - function

#  data cleaning
def clean_date(date_str):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    month = int(months.index(split_date[0]) + 1)
    day = int(split_date[1].split(',')[0])
    year = int(split_date[2])
    return datetime.date(year, month, day)

def clean_price(price_str):
    price_float = float(price_str)
    return (int(price_float * 100))
    
def add_csv():
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            title = row[0]
            author = row[1]
            date = clean_date(row[2])
            price = clean_price(row[3])
            new_book = Book(title=title, author=author, date_published=date, price=price)
            session.add(new_book)
        session.commit()

#  loop runs program
def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':
            # add_book()
            pass        
        elif choice == '2':
            #view books
            pass
        elif choice == '3':
            #search book
            pass
        elif choice == '4':
            #analysis
            pass
        else:
            print('GOODBYE')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    add_csv()

    for book in session.query(Book):
        print(book)



# def add_books(self):
#     self.title = input('What is the title of the book?\n')
#     self.author = input('Who is the author?\n')
#     self.date_published = input('What date was it published?\n')
#     self.price = input('What will it cost?\n')
#     new_book = models.Book(title='{self.title}',author='{self.author}',date_published='{self.date_published}',price='{self.price}')
# return models.session.add(new_book)