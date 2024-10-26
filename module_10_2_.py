import threading
import time
from threading import Thread
from time import sleep


class Knight(threading.Thread):
    lock = threading.Lock()

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали')
        enemy_power = 100
        number_days = 0
        while enemy_power > 0:
            time.sleep(1)
            number_days += 1
            enemy_power = max(0, enemy_power - self.power)
            with Knight.lock:
                print(f'{self.name} сражается {number_days} дней(дня), осталось {enemy_power} воинов.')

        with Knight.lock:
            print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')