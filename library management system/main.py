from random import randint
import json

storage_books_name = 'books_data_library.json'

# id(уникальный
# идентификатор, генерируется
# автоматически)
# • title(название
# книги)
# • author(автор
# книги)
# • year(год
# издания)
# • status(статус
# книги: “в
# наличии”, “выдана”)


def get_new_id(books_dict: dict) -> int:
    bias_mul_id = 10
    attempts = 10
    new_id = randint(10_000 * bias_mul_id, 100_000 * bias_mul_id)
    while True:
        bias_mul_id *= 10
        for _ in range(attempts):
            if new_id not in books_dict.keys():
                return new_id


class BookBase:
    def __init__(self, title, author, year, status):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

storege_books_name = 'books_data_library.json'

# Чтение словаря из файла
with open('books.json', 'r') as f:
    book_dict = json.load(f)

# Обновление словаря
new_id = get_new_id(book_dict)
book_dict[new_id] = {'title': 'Название книги', 'author': 'Автор книги'}

# Запись обновленного словаря обратно в файл
with open('books.json', 'w') as f:
    json.dump(book_dict, f)







