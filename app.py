# import models
from models import (Base, session, Book, engine)
import csv
import datetime
import time



def menu(): # main menu - add, search, analysis, exit, view 
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



def clean_date(date_str): # clean date
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
    split_date = date_str.split(' ')
    try:
        month = int(months.index(split_date[0]) + 1)
        day = int(split_date[1].split(',')[0])
        year = int(split_date[2])
        return_date = datetime.date(year, month, day)
    except ValueError:
        input('''
              \n****** DATE ERROR ******
              \rThe date format should include a valid Month, Day, year from the past.
              \rEx: January 13, 2003
              \rPress enter to try again.
              \r************************''')
        return
    except IndexError:
        input('''
              \n****** DATE ERROR ******
              \rThe date format should include a valid Month, Day, year from the past.
              \rEx: January 13, 2003
              \rPress enter to try again.
              \r************************''')
        return
    else:
        return return_date 

def clean_price(price_str): # clean price
    try:
        price_float = float(price_str)
    except ValueError:
        input('''
              \n****** PRICE ERROR ******
              \rThe price should be a number without a currency symbol.
              \rEx: 19.99
              \rPress enter to try again.
              \r*************************''')
        return
    else:
        return int(price_float * 100)

def clean_id(id_str, options): # clean id
    try:
        book_id = int(id_str)
    except ValueError:
        input('''
              \n****** ID ERROR ******
              \rThe id should be a number.
              \rPress enter to try again.
              \r*************************''')
        return
    else:
        if book_id in options:
            return book_id
        else:
            input(f'''
              \n****** ID ERROR ******
              \rOptions: {options}
              \rPress enter to try again.
              \r*************************''')
            return



def add_csv(): # reads / loads csv to db
    with open('suggested_books.csv') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            book_in_db = session.query(Book).filter(Book.title==row[0]).one_or_none()
            if book_in_db == None:
                title = row[0]
                author = row[1]
                date = clean_date(row[2])
                price = clean_price(row[3])
                new_book = Book(title=title, author=author, date_published=date, price=price)
                session.add(new_book)
        session.commit()


def app(): #  loop runs program
    app_running = True
    while app_running:
        choice = menu()
        if choice == '1':  # add book
            title = input('Title:  ')
            author = input('Author:  ')
            date_error = True
            while date_error:
                date = input('Date (Ex: March 13, 1992):  ')
                date = clean_date(date)
                if type(date) == datetime.date:
                    date_error = False
            price_error = True
            while price_error:    
                price = input('Price (Ex 19.99):  ')
                price = clean_price(price)
                if type(price) == int:
                    price_error = False
            new_book = Book(title=title, author=author, date_published=date, price=price) 
            session.add(new_book)
            session.commit()  
            print('Book Added!')
            time.sleep(1.5)      
        elif choice == '2': #view books
            for book in session.query(Book):
                print(f'{book.id} | {book.title} | {book.author}')
            input('\nPress enter to return to the main menu')
        elif choice == '3': #search book
            id_options = []
            for book in session.query(Book):
                id_options.append(book.id)
            id_error = True
            while id_error:
                id_choice = input(f'''
                    \nId Options: {id_options}
                    \rBook id: ''')    
                id_choice = clean_id(id_choice, id_options)
                if type(id_choice) == int:
                    id_error = False
            the_book = session.query(Book).filter(Book.id==id_choice)      
            print(f'''
                  \n{the_book.title} by {the_book.author}
                  \rPublished: {the_book.date_published}
                  \rPrice: ${the_book.price / 100}''')       
        elif choice == '4': # analysis
            pass
        else:
            print('GOODBYE')
            app_running = False


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()
    app()

