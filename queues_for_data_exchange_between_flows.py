from threading import Thread, Lock
from time import sleep
from queue import Queue



class Table:
    def __init__(self, number):
        self.number = number
        is_busy = False

class Cafe:
    def __init__(self, tables_list):
        self.tables = tables_list
        self.queue_customer = Queue()


    def customer_arrival(self):
        custom = Customer()
        for i in self.tables:
            if self.tables[i].is_busy:
        self.queue_customer.put(custom)



class Customer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        sleep(5)






Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
Customer - класс (поток) посетителя. Запускается, если есть свободные столы.

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

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()


    Атрибуты
    queue - очередь
    посетителей(создаётся
    внутри
    init), tables
    список
    столов(поступает
    из
    вне).
    Метод
    customer_arrival(self) - моделирует
    приход
    посетителя(каждую
    секунду).
    Метод
    serve_customer(self, customer) - моделирует
    обслуживание
    посетителя.Проверяет
    наличие
    свободных
    столов, в
    случае
    наличия
    стола - начинает
    обслуживание
    посетителя(запуск
    потока), в
    противном
    случае - посетитель
    поступает
    в
    очередь.Время
    обслуживания
    5
    секунд.

    number(int) - номер
    стола, is_busy(bool)














