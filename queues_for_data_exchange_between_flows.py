from threading import Thread, Lock
from time import sleep
from queue import Queue

lock = Lock()


class Table:
    def __init__(self, number):
        self.customer = None
        self.number = number
        self.is_busy = False

    def start_maintenance(self, customer):
        with lock:
            self.is_busy = True
            self.customer = customer
            self.customer.start()
            print(f'Посетитель {self.customer.number} сел за стол номер {self.number}')

    def is_complete_service(self):
        with lock:
            if self.customer is not None:
                if self.customer.is_alive():
                    return False
                else:
                    print('\033[92m'+f'Посетитель номер {self.customer.number} покушал и '
                          f'осводил стол номер {self.number}'+'\033[0m')
                    self.is_busy = False
                    return True
            else:
                return True


class Cafe:
    def __init__(self, tables_list):
        self.tables = tables_list
        self.queue_customer = Queue()
        self.customer_number = 0
        self.customer_are_still = True

    def customer_arrival(self, max_number_of_customer=20):
        while self.customer_number < max_number_of_customer:

            self.customer_number += 1

            custom = Customer(self.customer_number)
            print('\033[34m'+f'Посетитель номер {custom.number} прибыл'+'\033[0m')

            # Ищем индекс свободного столика
            ind = None
            for i in range(len(self.tables)):
                if not self.tables[i].is_busy:
                    ind = i
                    break

            if ind is None:
                self.queue_customer.put(custom)
                print(f'Посетитель {custom.number} ожидает свободный стол')
            else:
                self.tables[ind].start_maintenance(custom)

            sleep(1)

        self.customer_are_still = False

    def serve_customer(self):
        while self.customer_are_still or not self.queue_customer.empty():
            # Ищем столики на которых посетители завершили обслуживание
            for table in self.tables:
                if table.is_complete_service():
                    # Рассаживаем клиентов ждущих в очереди
                    if not self.queue_customer.empty():
                        custom = self.queue_customer.get()
                        table.start_maintenance(custom)
            sleep(0.2)


class Customer(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        sleep(5)


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Запускаем поток для обслуживания посетителей
serve_customer_thread = Thread(target=cafe.serve_customer)
serve_customer_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# Ожидаем завершения работы обслуживания посетителей
serve_customer_thread.join()
