from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Product(ABC):
    def __init__(self, name, price, amount):
        self._amount = amount
        self.name = name
        self.__price = price

    @property
    def get_amount(self):
        return self._amount

    def set_amount(self, value):
        if int(self._amount) >= 0:
            self._amount = value
        else:
            raise ValueError('Manfiy bolmasligi kerak')

    @property
    def get_price(self):
        return self.__price

    def set_price(self, value):
        if self.__price >= 0:
            self.__price = value
        else:
            raise ValueError('Manfiy bolmasligi kerak')

    @abstractmethod
    def add_amount(self, item):
        pass


class Product_kg(Product):
    def __init__(self, name, price, amount, weight):
        super().__init__(name, amount, price)
        self.weight = weight

    def add_amount(self, item):
        self._amount += item


class Product_lenghts(Product):
    def __init__(self, name, price, width, amount, length):
        super().__init__(name, amount, price)
        self.width = width
        self.length = length

    def add_amount(self, item):
        self._amount += item


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'


@dataclass
class People:
    name: str
    gender: Optional[Gender] = Gender.Male.value

    def printer(self):
        raise NotImplementedError(' bu parent class')


class Delivery(People):
    def __init__(self, name, gender, age, salary):
        super().__init__(name, gender)
        self._age = age
        self.__salary = salary

    @property
    def get_age(self):
        return self._age

    def set_age(self, value):
        if self._age >= 0:
            self._age = value
        else:
            raise ValueError('Manfiy bolmasligi kerak')

    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        if self.__salary >= 0:
            self.__salary = value
        else:
            raise ValueError('Manfiy bolmasligi kerak')

    def printer(self):
        print(f"ismi: {self.name}\n"
              f"yoshi {self.get_age}\n"
              f"gender {self.gender}")


class Customer(People):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.orders = []

    def printer(self):
        print(f"ismi: {self.name}\n"
              f"gender {self.gender}")
        for x in self.orders:
            print(f'zakaz: {x.name}, narxi {x.get_price}')


class UzumMarket:
    def __init__(self):
        self.money = 0
        self.customer = []

    def customer_adder(self, customer: Customer):
        self.customer.append(customer)

    def create_order_kg(self, customer: Customer, product_kg: Product_kg, son):
        if son <= int(product_kg.get_amount):
            customer.orders.append(product_kg)
            self.money += product_kg.get_price
            product_kg.set_amount(int(product_kg.get_amount)-son)
        else:
            print('Maxsulot soni siz Kiritgan sondan kam')

    def create_order_lenghts(self, customer: Customer, product_lenghts: Product_lenghts, son):
        if son <= int(product_lenghts.get_amount):
            customer.orders.append(product_lenghts)
            self.money += product_lenghts.get_price
            product_lenghts.set_amount(int(product_lenghts.get_amount)-son)
        else:
            print('Maxsulot soni siz Kiritgan sondan kam')
    def printer(self):
        for x in self.customer:
            print(f'marketdagi xaridor: {x.name}')
        print(f' marketdagi daromad {self.money}')


pro_kg1 = Product_kg('Olma', 12000, 7, 10)
pro_kg2 = Product_kg('Olcha', 25000, 5, 8)

pro_len1 = Product_lenghts('shlanka', '50000', '15', 5, '300')
pro_len2 = Product_lenghts('taxta', '80000', '20', 6, '500')

deli_ver1 = Delivery('Akbar', Gender.Male.value, 15,45000)
deli_ver2 = Delivery('Aziza', Gender.Female.value, 20,50000)

Cust1 = Customer('Abbos', Gender.Male.value)
Cust2 = Customer('Malika', Gender.Female.value)

for x in [deli_ver1, deli_ver2, Cust1, Cust2]:
    x.printer()

market = UzumMarket()

market.customer_adder(Cust1)
market.customer_adder(Cust2)
market.create_order_kg(Cust1, pro_kg1, 2)
market.create_order_kg(Cust2, pro_kg1, 5)
market.create_order_kg(Cust1, pro_kg2, 2)
market.create_order_kg(Cust2, pro_kg2, 2)


market.create_order_lenghts(Cust1, pro_len1, 2)
market.create_order_lenghts(Cust2, pro_len1, 5)
market.create_order_lenghts(Cust1, pro_len2, 2)
market.create_order_lenghts(Cust2, pro_len2, 2)


market.printer()











