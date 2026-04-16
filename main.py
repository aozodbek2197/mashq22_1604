# 1-mashq
from abc import ABC, abstractmethod
from datetime import date

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self._is_available = True
    
    @abstractmethod
    def get_info(self): pass

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    
    def get_info(self):
        return f"Kitob: {self.title} - {self.author}"
    
    def borrow(self):
        if self._is_available:
            self._is_available = False
            print(f"{self.title} berildi.")
        else:
            print("Kitob band.")

class Library:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def show_available(self):
        for item in self.items:
            if item._is_available:
                print(item.get_info())

lib = Library()
lib.add_item(Book("Python OOP", "Mark Lutz"))
lib.add_item(Book("Clean Code", "Robert Martin"))
lib.items[0].borrow()
lib.show_available()
# 2-mashq
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def sell(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            return self.price * qty
        return 0

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, qty):
        self.items.append((product, qty))
    
    def total(self):
        return sum(p.sell(q) for p, q in self.items)

cart = ShoppingCart()
p1 = Product("Telefon", 5000000, 10)
p2 = Product("Quloqchin", 300000, 20)
cart.add_product(p1, 1)
cart.add_product(p2, 2)
print("Jami:", cart.total())
# 3-mashq
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self, target): pass

class Warrior(Character):
    def attack(self, target):
        damage = 30
        target.health -= damage
        print(f"{self.name} qilich bilan {target.name}ga {damage} zarar yetkazdi.")

class Mage(Character):
    def attack(self, target):
        damage = 45
        target.health -= damage
        print(f"{self.name} sehr bilan {target.name}ga {damage} zarar yetkazdi.")

hero = Warrior("Aragorn", 100)
enemy = Mage("Saruman", 80)
hero.attack(enemy)
print(f"{enemy.name} sog'lig'i: {enemy.health}")
# 4-mashq
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self): pass

class SportsCar(Car):
    def drive(self): print("Tez sport mashina yurdi!")

class FamilyCar(Car):
    def drive(self): print("Oilaviy mashina tinch yurdi.")

class ElectricCar(Car):
    def drive(self): print("Elektromobil jim yurdi.")

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "sports": return SportsCar()
        elif car_type == "family": return FamilyCar()
        elif car_type == "electric": return ElectricCar()
        raise ValueError("Noto'g'ri tur")

factory = CarFactory()
car = factory.create_car("electric")
car.drive()
# 5-mashq
class FileSystemEntity:
    def __init__(self, name):
        self.name = name

class File(FileSystemEntity):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
    def show(self):
        print(f"Fayl: {self.name} ({self.size} KB)")

class Folder(FileSystemEntity):
    def __init__(self, name):
        super().__init__(name)
        self.children = []
    
    def add(self, entity):
        self.children.append(entity)
    
    def show(self, level=0):
        print("  " * level + f"Papka: {self.name}")
        for child in self.children:
            child.show(level + 1)

root = Folder("Root")
docs = Folder("Documents")
root.add(docs)
docs.add(File("report.txt", 45))
root.show()
