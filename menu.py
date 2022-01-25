from app import books

USER_CHOICE = """
    a - for best books 
    b - for best and best priced best_book
    n - next available book
    q - quit
"""


def best_books():
    sliced = 10
    best_books = sorted(books, key=lambda x: x.rating * -1)[:sliced] #-1 to reverse the listing best to worst
    for book in best_books:
        print(book)


def best_books_and_price():
    sliced = 10
    best_books_by_price = sorted(books, key=lambda x: {x.rating, x.price})[:sliced] #-1 to reverse the listing best to worst
    for book in best_books_by_price:
        print(book)


books_gen = (i for i in books)


def get_next_book():
    print(next(books_gen))


user_choices = {
    'a': best_books,
    'b': best_books_and_price,
    'n': get_next_book
}


def choices():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in user_choices:
            selected_menu_function = user_choices[user_input]
            selected_menu_function()
        else:
            print('unknown command')
        user_input = input(USER_CHOICE)


choices()