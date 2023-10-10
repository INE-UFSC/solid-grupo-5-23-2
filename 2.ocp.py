"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):

    def make_sound(self):
        print('roar')

class Mouse(Animal):

    def make_sound(self):
        print('squeak')

animals = [
    Lion(),
    Mouse()
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)

"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Customer(ABC):

    def __init__(self, discount) -> None:
        self.__discount = discount
    
    @property
    def discount(self):
        return self.__discount
    
class CustomerVIP(Customer):

    def __init__(self) -> None:
        super().__init__(0.4)

class CustomerFAV(Customer):

    def __init__(self, discount) -> None:
        super().__init__(0.2)
    
class Discount:
    def __init__(self, customer: Customer, price: float):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * self.customer.discount
