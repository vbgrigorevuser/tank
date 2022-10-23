'''
    Модуль tank.py, который содержит класс, отвественный за логику
    танков в игре
'''
import random

class Tank:
    '''Класс Tank, имеет два главных метода print_info и shot'''

    def __init__(self, model, armor, min_damage, max_damage, health):
        '''Метод, инициализирующий танки'''
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self):
        '''Вывод информации о танке'''
        print(f'{self.model} имеет лобовую броню {self.armor:.2f} мм' +
              f' при {self.health:.2f} ед. здоровья и урон в {self.damage} единиц')

    def health_down(self, damage):
        '''Вспомогательный метод пересчета здоровья после выстрела'''
        self.health -= damage / self.armor
        print(f'{self.model}: Командир, по экипажу {self.model} попали, у нас осталось ' +
              f'{self.health if self.health > 0 else 0:.2f} очков здоровья')

    def shot(self, enemy):
        '''Метод shot для реализации выстрела в танк enemy'''
        enemy.health_down(self.damage)
        if enemy.health <= 0:
            print(f'Экипаж танка {enemy.model} уничтожен')
        else:
            print(f'{self.model}: Точно в цель, у противника {enemy.model} ' +
                  f'осталось {enemy.health if enemy.health > 0 else 0:.2f} единиц здоровья')
