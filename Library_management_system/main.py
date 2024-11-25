from command_line_sub_menu import SubMenu
from custom_string import CustomString

text_welcome = "Добро пожаловать в систему управления библиотекой!"


class Menu(SubMenu):
    def __init__(self):
        super().__init__()
        self.valid_selection_symbol = ('a', 'd', 'f', 'p', 's', 'q')
        self.choice_message = f"\tдобавление книги\t'{self.valid_selection_symbol[0]}'\n" \
                              f"\tудаление книги\t'{self.valid_selection_symbol[1]}'\n" \
                              f"\tпоиск книги\t'{self.valid_selection_symbol[2]}'\n" \
                              f"\tотображение всех книг\t'{self.valid_selection_symbol[3]}'\n" \
                              f"\tизменение статуса книги\t'{self.valid_selection_symbol[4]}'\n" \
                              f"\tвыход из программы\t'{self.valid_selection_symbol[5]}'\n"
        self.invalid_message = "Не понял выбор!"

    def run_choose(self):
        choice = ''
        while choice != self.valid_selection_symbol[5]:
            print(self.cs.info("Доступны следующие команды библиотеки, введите соответствующий символ для выбора:"))
            while True:
                choice = input(self.choice_message)

                if choice in self.valid_selection_symbol:
                    break
                else:
                    print(self.cs.warning(f'{self.invalid_message}'))

            if choice == self.valid_selection_symbol[0]:
                self.add_book()
            elif choice == self.valid_selection_symbol[1]:
                self.delete_book()
            elif choice == self.valid_selection_symbol[2]:
                self.find_book()
            elif choice == self.valid_selection_symbol[3]:
                self.print_all_books()
            elif choice == self.valid_selection_symbol[4]:
                self.change_status()
            elif choice == self.valid_selection_symbol[5]:
                break
            else:
                break


if __name__ == '__main__':
    cs = CustomString()
    print(cs.welcome(text_welcome))
    menu = Menu()
    menu.run_choose()
