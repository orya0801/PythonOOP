from abc import ABC, abstractmethod

"""
    Класс Dish - абстрактный класс, содержащий 2 метода - info и cook. Эти методы 
    должны переопределяться при создании нового класса блюда. 
"""


class Dish:

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def cook(self):
        pass
