class Factory:
    def __init__(self, name):
        self.name = name


class Car(Factory):
    def __init__(self, name, cost):
        super().__init__(name)
        self.__cost = cost

    @property
    def get_cost(self):
        return self.__cost

    def set_cost(self, cost):
        if cost > 0:
            self.__cost = cost
        else:
            raise ValueError('cost 0 dan katta bolishi kerak')


class Worker(Factory):
    def __init__(self, name, age, salary):
        super().__init__(name)
        self._age = age
        self.__salary = salary

    @property
    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError('age 0 dan katta bolishi kerak')

    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError('salary 0 dan katta bolishi kerak')


car1 = Car('Camaro', '15000')
car2 = Car('F150', '25000')

work = Worker('Aby', '45', '5000')
work1 = Worker('Aby', '45', '5000')

print(f"before {car1.name}, Cost: {car1.get_cost}")
print(f"before {car2.name}, Cost: {car2.get_cost}")

print(f'before {work.name} age: {work.get_age}, {work.get_salary}')
print(f'before {work1.name} age: {work1.get_age}, {work1.get_salary}')

car1.set_cost(20000)
car2.set_cost(30000)

work.set_age(30)
work.set_salary(2500)
work1.set_age(35)
work1.set_salary(3000)


print(f"after {car1.name}, Cost: {car1.get_cost}")
print(f"after {car2.name}, Cost: {car2.get_cost}")

print(f'after {work.name} age: {work.get_age}, {work.get_salary}')
print(f'after {work1.name} age: {work1.get_age}, {work1.get_salary}')


############################################################# 2 #######################################################

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self._year = year
        self.__odometer = 0



    def get_year(self):
        return self._year

    def set_year(self, year):
        if year > 0:
            return self._year


    def get_odometer(self):
        return self.__odometer


    def increasing_odometer(self, miles):
        self.__odometer += miles


car = Car("Mercedes", "GLS", "2024")
car1 = Car("Audi", 'TT', '2024')

print(f'before {car.make}, {car.model}, {car.get_year()}, {car.get_odometer()}')
print(f'before {car1.make}, {car1.model}, {car1.get_year()}, {car1.get_odometer()}')

car.set_year(2025)
car.increasing_odometer(30000)


car1.set_year(2025)
car1.increasing_odometer(30000)


print(f'after {car.make}, {car.model}, {car.get_year()}, {car.get_odometer()}')
print(f'after {car1.make}, {car1.model}, {car1.get_year()}, {car1.get_odometer()}')


############################################################# 3 #######################################################


class Company:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > self._age:
            self._age = age


class Teachers(Company):
    def __init__(self, age, name, ielts, salary):
        super().__init__(name, age)
        self.__ielts = ielts
        self.__salary = salary

    def get_ielts(self):
        return self.__ielts

    def set_ielts(self, ielts):
        if ielts > 0:
            self.__ielts = ielts

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary


teach = Teachers(25, 'Alice', '9', '5000')
teach1 = Teachers(30, 'Sarah', '8', '6000')

print(f"before her age was {teach.get_age()} and {teach.name} got {teach.get_ielts()}, and her salary was {teach.get_salary()}")
print(f"before her age was {teach1.get_age()} and {teach1.name} got {teach1.get_ielts()}, and her salary was {teach1.get_salary()}")


teach.set_age(30)
teach1.set_age(35)
teach.set_ielts(10)
teach1.set_ielts(9)
teach.set_salary(8000)
teach1.set_salary(9000)


print(f"after her age was {teach.get_age()} and {teach.name} got {teach.get_ielts()}, and her salary was {teach.get_salary()}")
print(f"after her age was {teach1.get_age()} and {teach1.name} got {teach1.get_ielts()}, and her salary was {teach1.get_salary()}")











