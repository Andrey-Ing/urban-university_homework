import books_data_library_control as bc


class InputInfoBook:
    title_min_max_length = 1, 200
    autor_min_max_length = 1, 100
    year_min_max = -7000, 3000
    acceptable_status_book = 'н', 'в'
    invalid_message = '\033[31mНе понял ввод!\033[0m'
    invalid_id_message = '\033[31mНеверный идентификатор! ID должен содержать две буквы, дефис и число\033[0m'

    def get_title(self):
        title = str(input("Введите название книги: "))
        while not self.title_min_max_length[0] <= len(title) <= self.title_min_max_length[1]:
            print(f"{self.invalid_message}\n"
                  f"Введите название книги от {self.title_min_max_length[0]} "
                  f"до {self.title_min_max_length[1]} символов")
            title = str(input("Название книги: "))
        return title

    def get_author(self):
        autor = str(input("Введите автора: "))
        while not self.autor_min_max_length[0] <= len(autor) <= self.autor_min_max_length[1]:
            print(f"{self.invalid_message}\n"
                  f"Введите автора от {self.autor_min_max_length[0]} "
                  f"до {self.autor_min_max_length[1]} символов")
            autor = str(input("Автор: "))
        return autor

    def get_year(self):
        year = input("Введите год издания: ")
        while not (year.lstrip('-').isdigit() and self.year_min_max[0] <= int(year) <= self.year_min_max[1]):
            print(f"{self.invalid_message}\n"
                  f"Введите год от {self.year_min_max[0]} до {self.year_min_max[1]}")
            year = input("Год издания: ")
        return int(year)

    def get_status(self):
        status = input(f"Введите статус книги '{self.acceptable_status_book[0]}' (в наличии) или "
                       f"'{self.acceptable_status_book[1]}' (выдана): ")
        while status not in self.acceptable_status_book:
            status = input(f"{self.invalid_message}\n"
                           f"Нужно ввести '{self.acceptable_status_book[0]}' (в наличии) или "
                           f"'{self.acceptable_status_book[1]}' (выдана): ")
        return True if status == self.acceptable_status_book[0] else False

    def get_id(self):
        id_book = input("Введите ID книги: ")
        while len(id_book) < 4 or not (id_book[:2].isalpha() and id_book[2] == '-' and id_book[3:].isdigit()):
            print(self.invalid_id_message)
            id_book = input("Введите ID: ")
        return id_book


class SubMenu(InputInfoBook):
    def __init__(self):
        super().__init__()

    def add_book(self):
        pass

    def delete_book(self):
        id_book = self.get_id()
        if bc.delete_book_in_library(id_book):
            print(f"Книга с ID: {id_book} успешно удалена")
            return True
        else:
            print('\033[31m' + f"Книга с ID: {id_book} не удалена (возможно, такой книги не существует)" + '\033[0m')
            return False

    def find_book(self):
        valid_selection_symbol = ('t', 'a', 'y')
        invalid_message = '\033[31mНе понял выбор!\033[0m'
        while True:
            choice = input("Для поиска книги:\n"
                           f"\tпо названию введите '{valid_selection_symbol[0]}'\n"
                           f"\tпо автору введите '{valid_selection_symbol[1]}'\n"
                           f"\tпо году введите '{valid_selection_symbol[2]}'\n").lower()

            if choice in valid_selection_symbol:
                break
            else:
                print(f'{invalid_message}')

        if choice == valid_selection_symbol[0]:
            title = self.get_title()
            return bc.find_book_in_library(title=title)
        elif choice == valid_selection_symbol[1]:
            author = self.get_author()
            return bc.find_book_in_library(author=author)
        elif choice == valid_selection_symbol[2]:
            year = self.get_year()
            return bc.find_book_in_library(year=year)

    @staticmethod
    def print_all_books():
        books_dict = bc.get_all_books_in_library()
        for id_book, book in books_dict.items():
            print('\033[33m' '*' * 15, '\033[0m' '\n'
                  '\033[1m' + 'ID книги:\t' + f'{id_book}' + '\033[0m\n'
                  f"Название:\t{book[bc.BookBase.title_idx]}\n"
                  f"Автор:\t\t{book[bc.BookBase.author_idx]}\n"
                  f"Год издания:\t{book[bc.BookBase.year_idx]}\n"
                  f"{'\033[32m' + 'в наличии' + '\033[0m' if book[bc.BookBase.status_idx] else
                     '\033[31m' + 'выдана' + '\033[0m'}\n")

        print('\033[44m' + f'Всего книг в библиотеке: {len(books_dict)}' + '\033[0m')

    def change_status(self):
        pass
