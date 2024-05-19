from multiprocessing import Process, Value


class WarehouseManager:
    def __init__(self):
        self.data = dict()
        self.process_data = dict()

    def process_data_update(self, reqs):
        for req in reqs:
            self.process_data[req[0]] = Value('i', 0)

    def convert_process_data_to_data(self):
        for key in self.process_data:

            if self.process_data[key].value < 0:
                raise ValueError(f'Invalid Request, запрошено товара {key} на {abs(self.process_data[key].value)} '
                                 f'больше, чем было на складе')

            self.data[key] = self.process_data[key].value

    def process_request(self, reqs):

        if reqs[1] == 'receipt':
            self.process_data[reqs[0]].value += reqs[2]

        elif reqs[1] == 'shipment':
            self.process_data[reqs[0]].value -= reqs[2]

        else:
            raise NameError(f'Invalid Request (непонятно ({reqs[1]}), что делать с товаром)')

    def run(self, requests_list):

        self.process_data_update(requests_list)

        for req in requests_list:
            proc = Process(target=self.process_request, args=(req,), daemon=True)
            proc.start()
            proc.join()

        self.convert_process_data_to_data()


if __name__ == '__main__':

    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 120),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 60),
        ("product1", "shipment", 30),
        ("product3", "receipt", 10),
        ("product2", "shipment", 40),
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(manager.data)
