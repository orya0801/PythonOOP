"""
    Трехуровневая архитектура разделяет приложение на уровни абстракции:
    1. Уровень хранения данных
    2. Уровень бизнес-логики
    3. Уровень представления
"""


class Database:
    """ Data Store Class """
    pizzas = {
        "Default": {
            "small": 0,
            "middle": 0,
            "large": 0
        },
        "BBQ": {
            "small": 300,
            "middle": 400,
            "large": 470
        },
        "Margarita": {
            "small": 200,
            "middle": 300,
            "large": 370
        },
        "Pepperoni": {
            "small": 320,
            "middle": 410,
            "large": 480
        }
    }

    def __get__(self, instance, owner):
        return {'pizzas': self.pizzas}


class SingletonMeta(type):
    """
        В Python класс Одиночка можно реализовать по-разному. Возможные способы
        включают себя базовый класс, декоратор, метакласс. Мы воспользуемся
        метаклассом, поскольку он лучше всего подходит для этой цели.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class DatabaseWorker(metaclass=SingletonMeta):
    """
        Описание бизнес-логики одиночки,
        которая может быть выполнена на его экземпляре
    """

    db = Database()

    def pizza_list(self):
        return self.db['pizzas'].keys()

    def get_pizza_prices(self, name):
        return self.db['pizzas'][name]

    def get_pizza_price(self, name, size):
        return self.db['pizzas'][name][size]


# Test
dbworker = DatabaseWorker()
dbworker1 = DatabaseWorker()
pizza_price = dbworker.get_pizza_price("BBQ", "large")
print(pizza_price)
