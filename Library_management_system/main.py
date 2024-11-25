from command_line_sub_menu import SubMenu

text_welcome = '\033[43m'"Добро пожаловать в систему управления библиотекой!" '\033[0m'


class Menu(SubMenu):
    valid_selection_symbol = ('a', 'd', 'f', 'p', 's', 'q')
    choice_message = f"\tдобавление книги\t'{valid_selection_symbol[0]}'\n" \
                     f"\tудаление книги\t'{valid_selection_symbol[1]}'\n" \
                     f"\tпоиск книги\t'{valid_selection_symbol[2]}'\n" \
                     f"\tотображение всех книг\t'{valid_selection_symbol[3]}'\n" \
                     f"\tизменение статуса книги\t'{valid_selection_symbol[4]}'\n" \
                     f"\tвыход из программы\t'{valid_selection_symbol[5]}'\n"
    invalid_message = '\033[31mНе понял выбор!\033[0m'

    def __init__(self):
        super().__init__()

    def run_choose(self):
        choice = ''
        while choice != self.valid_selection_symbol[5]:
            print("Доступны следующие команды библиотеки, введите соответствующий символ для выбора:")
            while True:
                choice = input(self.choice_message)

                if choice in self.valid_selection_symbol:
                    break
                else:
                    print(f'{self.invalid_message}')

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
    print(text_welcome)
    menu = Menu()
    menu.run_choose()








