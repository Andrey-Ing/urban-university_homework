from threading import Thread, Lock
from time import sleep


class BankAccount:
    def __init__(self, lock_object, check=0):
        self.lock = lock_object
        self.check = check

    def deposit(self, amount):
        with lock:
            self.check += amount
            sleep(0.1)  # чтобы был виден эффект если убрать lock
            print(f'Deposited {amount}, new balance is {self.check}')

    def withdraw(self, amount):
        with lock:
            self.check -= amount
            sleep(0.1)  # чтобы был виден эффект если убрать lock
            print(f'Withdrew {amount}, new balance is {self.check}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


lock = Lock()
bk_account = BankAccount(lock, 1000)

deposit_thread = Thread(target=deposit_task, args=(bk_account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(bk_account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
