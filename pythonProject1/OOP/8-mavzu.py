class Animal:
    def make_sound(self):
        raise NotImplementedError('make_sound method not implemented')

    def eating(self):
        raise NotImplementedError('eating method not implemented')


class Dog(Animal):
    def make_sound(self):
        return 'Bark'

    def eating(self):
        return 'The dog is eating chicken'


class Kangaroo(Animal):
    def make_sound(self):
        return 'Tsi-tsi'

    def eating(self):
        return 'The kangaroo is eating grass and leaves'


class Bird(Animal):
    def make_sound(self):
        return 'Chirp-chirp!'

    def eating(self):
        return 'The bird is eating seeds'



def animal_behavior(animal):
    print(animal.make_sound())
    print(animal.eating())


dog = Dog()
kangaroo = Kangaroo()
bird = Bird()


print("Actions of the Dog:")
animal_behavior(dog)

print("\nActions of the Kangaroo:")
animal_behavior(kangaroo)

print("\nActions of the Bird:")
animal_behavior(bird)


################################################################  2  ##############################################

class Payment:
    def pay(self):
        raise NotImplementedError('pay method not implemented')

    def refund(self):
        raise NotImplementedError('refund method not implemented')


class CreditCard(Payment):
    def pay(self):
        return ' payment made by Credit card '

    def refund(self):
        return 'Refund started to Credit Card'


class PayPal(Payment):
    def pay(self):
        return 'Payment made by PayMe'

    def refund(self):
        return 'Refund started to PayMe'


class Bitcoin(Payment):
    def pay(self):
        return 'Payment made by Click'

    def refund(self):
        return 'Refund started to Click'


def process_payment(payment):
    print(payment.pay())
    print(payment.refund())



credit_card = CreditCard()
paypal = PayPal()
bitcoin = Bitcoin()


print("Credit Card:")
process_payment(credit_card)

print("\nPayMe:")
process_payment(paypal)

print("\nClick:")
process_payment(bitcoin)




################################################################  3  ##############################################


class Vehicle:
    def start_engine(self):
        raise NotImplementedError('start_engine method not implemented')

    def stop_engine(self):
        raise NotImplementedError('stop_engine method not implemented')


class Sedan(Vehicle):
    def start_engine(self):
        return 'Car engine started'

    def stop_engine(self):
        return 'Car engine stopped'


class Motorcycle(Vehicle):
    def start_engine(self):
        return 'Motorcycle engine started'

    def stop_engine(self):
        return 'Motorcycle engine stopped'


class SUV(Vehicle):
    def start_engine(self):
        return 'Truck engine started'

    def stop_engine(self):
        return 'Truck engine stopped'


def vehicle_operations(vehicle):
    print(vehicle.start_engine())
    print(vehicle.stop_engine())


car = Sedan()
motorcycle = Motorcycle()
SUV = SUV()


print("Sedan:")
vehicle_operations(Sedan)

print("\nMotorcycle:")
vehicle_operations(motorcycle)

print("\nSUV:")
vehicle_operations(SUV)

