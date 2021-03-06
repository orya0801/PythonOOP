import time, types
from functools import wraps

"""
    PizzaMetaclass предназначен для отслеживания типов создаваемых объектов
    при выполнении программы. С помощью его можно понять последовать выполнения
    методов __new__, __init__ и __call__ для отлавливания ошибок при преобразовании
    типов. 
"""


class PizzaMetaclass(type):
    def __new__(cls, class_name, parents, attributes):
        print('- PizzaMetaclass__new__ - Creating class instance of type ', cls)
        return super().__new__(cls, class_name, parents, attributes)

    def __init__(self, class_name, parents, attributes):
        print('- PizzaMetaclass.__init__ - Initializing the class instance', self)
        super().__init__(class_name, parents, attributes)

    def __call__(self, *args, **kwargs):
        print('- PizzaMetaclass.__call__ - Creating object of type ', self)
        return super().__call__(*args, **kwargs)



