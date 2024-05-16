from threading import Thread, Lock
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.customer = None
        self.number = number
        self.is_busy = False

    def start_maintenance(self, customer):
        is_busy = True
        self.customer = customer
        self.customer.start()
        print(f'Посетитель {self.customer.number} сел за стол номер {self.number}')

    def is_complete_service(self):
        if self.customer is not None:
            if self.customer.isAlive():
                return False
            else:
                print(f'Посетитель номер {self.customer.customer_number} покушал и'
                      f'осводил стол номер {self.number}')
                is_busy = False
                return True
        else:
            return True


class Cafe:
    def __init__(self, tables_list):
        self.tables = tables_list
        self.queue_customer = Queue()
        self.customer_number = 0
        self.customer_are_still = True

    def customer_arrival(self, max_number_of_customer = 20):
        while self.customer_number <= max_number_of_customer:

            self.customer_number += 1

            custom = Customer(self.customer_number)
            print(f'Посетитель номер {custom.number} прибыл')

            # Ищем свободный столик

            for i in range(self.tables):
                if self.tables[i].is_busy


            ind = next((x for x in self.tables if x.is_busy is False), None)

            if ind is None:
                self.queue_customer.put(custom)
                print(f'Посетитель {custom.number} ожидает свободный стол')
            else:
                self.tables[ind].start_maintenance(custom)

            sleep(1)

        self.customer_are_still = False


    def serve_customer(self):
        while self.customer_are_still and not self.queue_customer.empty():
            # Ищем столики на которых посетители завершили обслуживание
            for table in self.tables:
                if table.is_complete_service(self):
                    # Рассаживаем клиентов ждущих в очереди
                    if not self.queue_customer.empty():
                        custom = self.queue_customer.get()
                        table.start_maintenance(custom)


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
