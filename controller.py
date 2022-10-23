'''
    Модуль controller.py, отвественный за управление игрой
'''

from tank import Tank
from time import sleep

class Controller:
    '''Класс Controller начинает игру и контролирует ее процесс'''

    def __init__(self):
        model_1 = input('Игрок 1, введи модель своего танка: ')
        model_2 = input('Игрок 2, введи модель своего танка: ')
        self.tank1 = Tank(model_1, 10, 1, 9, 10)
        self.tank2 = Tank(model_2, 10, 1, 9, 10)

    def main_loop(self):
        while True:
            self.tank1.shot(self.tank2)
            sleep(1)
            if self.tank2.health <= 0:
                print(f'{self.tank1.model} победил!')
                break
            self.tank2.shot(self.tank1)
            sleep(1)
            if self.tank1.health <= 0:
                print(f'{self.tank2.model} победил!')
                break
