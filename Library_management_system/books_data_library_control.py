import re
from random import randint
import json

storage_books_name = 'books_data_library.json'


def get_new_id(books_dict: dict) -> str:
    prefix_chr = chr(randint(ord('A'), ord('Z'))) + chr(randint(ord('A'), ord('Z')))
    bias_mul_id = 10
    attempts = 10
    while True:
        bias_mul_id *= 10
        for _ in range(attempts):
            postfix_number = randint(100 * bias_mul_id, 1000 * bias_mul_id)
            new_book_id = prefix_chr + '-' + str(postfix_number)
            if new_book_id not in books_dict:
                return new_book_id


class BookBase:
    def __init__(self, title: str, author: str, year: int, status: bool = True):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def get_serial_data(self):
        return [self.title, self.author, self.year, self.status]

    title_idx = 0
    author_idx = 1
    year_idx = 2
    status_idx = 3


def _library_read_data(filename: str) -> dict:
    with open(filename, 'r') as stor_r:
        data = json.load(stor_r)
        return data


def _library_save_data(filename: str, data: dict):
    with open(filename, 'w') as stor_w:
        json.dump(data, stor_w, indent=4)


def add_book_in_library(book: BookBase) -> str:
    data_books = _library_read_data(storage_books_name)
    new_id = get_new_id(data_books)
    data_books[new_id] = book.get_serial_data()
    _library_save_data(storage_books_name, data_books)
    return new_id


def delete_book_in_library(book_id: str) -> bool:
    data_books = _library_read_data(storage_books_name)
    if book_id in data_books:
        del data_books[book_id]
        _library_save_data(storage_books_name, data_books)
        return True
    else:
        return False


def find_book_in_library(title: str = None, author: str = None, year: str = None) -> list:
    result = []
    data_books = _library_read_data(storage_books_name)
    try:
        if title is not None:
            for book_id, book in data_books.items():
                if re.fullmatch(title, book[BookBase.title_idx]):
                    result.append(book_id)
        if author is not None:
            for book_id, book in data_books.items():
                if re.fullmatch(author, book[BookBase.author_idx]):
                    result.append(book_id)
        if year is not None:
            for book_id, book in data_books.items():
                if re.fullmatch(str(year), str(book[BookBase.year_idx])):
                    result.append(book_id)

        return result
    except re.error:
        return list()


def get_all_books_in_library() -> dict:
    return _library_read_data(storage_books_name)


def change_book_status(book_id: str, status: bool) -> bool:
    data_books = _library_read_data(storage_books_name)
    if book_id in data_books:
        data_books[book_id][BookBase.status_idx] = status
        _library_save_data(storage_books_name, data_books)
        return True
    else:
        return False


def get_book_from_id(book_id: str) -> BookBase:
    data_books = _library_read_data(storage_books_name)
    if book_id in data_books:
        book_data = data_books[book_id]
        return BookBase(book_data[BookBase.title_idx],
                        book_data[BookBase.author_idx],
                        book_data[BookBase.year_idx],
                        book_data[BookBase.status_idx])
    else:
        raise (KeyError(f"Book with id {book_id} not found"))
