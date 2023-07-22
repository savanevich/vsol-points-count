from app import books

USER_CHOICE = '''Enter one of the following:

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''

books_generator = (x for x in books)


def print_best_books():
    print('Printing best books...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)


def print_cheapest_books():
    print('Printing cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


def print_next_book():
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Invalid command. Please try again.')

        user_input = input(USER_CHOICE)


menu()
