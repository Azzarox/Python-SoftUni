book_wanted = input()
book_count = 0

while True:
    new_book = input()

    if new_book == book_wanted:
        print(f'You checked {book_count} books and found it.')
        break
    if new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f'You checked {book_count} books.')
        break
    book_count += 1      #nai-otdolu za da ne otchita poslednata kniga(toest namerenata)
