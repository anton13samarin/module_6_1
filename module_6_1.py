class Animal:                   # Класс ЖИВОТНЫЕ
    def __init__(self,name):    # Функция создания объекта
        self.alive = True       # Создания атрибута по умолчанию ЖИВОЙ = ПРАВДА
        self.fed = False        # Создание атрибута по умолчанию НАКОРМЛЕННЫЙ = ЛОЖЬ
        self.name = name        # Создание атрибута ИМЯ

class Mammal(Animal):           # Класс МЛЕКОПИТАЮЩЕЕ - наследует атрибуты и методы от класса ЖИВОТНЫЕ
    def eat (self,food):        # Создаем метод КУШАТЬ
        if food.edible:         # Условие метода если ЕДА СЪЕДОБНАЯ
            print(f"{self.name} съел {food.name}")  # Вывести ...
            self.fed = True     # Изменить атрибут НАКОРМЛЕННЫЙ класса ЖИВОТНЫЕ на ПРАВДА
        else:                   # Иначе
            print(f"{self.name} не стал есть {food.name}")  # Вывести ...
            self.alive = False  # Изменить атрибут НАКОРМЛЕННЫЙ класса ЖИВОЙ на ЛОЖЬ

class Predator(Animal):         # Класс ХИЩНИК - наследует атрибуты и методы от класса ЖИВОТНЫЕ
    def eat (self,food):        # Создаем метод КУШАТЬ
        if food.edible:         # Условие метода если ЕДА СЪЕДОБНАЯ
            print(f"{self.name} съел {food.name}")  # Вывести ...
            self.fed = True     # Изменить атрибут НАКОРМЛЕННЫЙ класса ЖИВОТНЫЕ на ПРАВДА
        else:                   # Иначе
            print(f"{self.name} не стал есть {food.name}")  # Вывести ...
            self.alive = False  # Изменить атрибут НАКОРМЛЕНН класса ЖИВОЙ на ЛОЖЬ

class Plant:                    # Класс РАСТЕНИЕ
    def __init__(self,name):    # Функция создания объекта
        self.edible = False     # Создания атрибута по умолчанию СЪЕДОБНОЕ = ЛОЖЬ
        self.name = name        # Создание атрибута ИМЯ

class Flower(Plant):            # Класс ЦВЕТОК - наследует атрибуты и методы от класса РАСТЕНИЕ
    pass                        # Ставим заглушку, так как значение совпадает со значением РАСТЕНИЕ по умолчанию

class Fruit(Plant):             # Класс ФРУКТ
    def __init__(self, name):   # Функция создания объекта
        super().__init__(name)  # Вызываем конструктор родительского класса РАСТЕНИ
        self.edible = True      # Изменить атрибут СЪЕДОБНЫЙ класса РАСТЕНИЕ на ПРАВДВ


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')


print(a1.name)
print(p1.name)


print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)