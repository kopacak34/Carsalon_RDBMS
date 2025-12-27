class Customer:
    def __init__(self, id, name, email, active):
        self.id = id
        self.name = name
        self.email = email
        self.active = active


class Car:
    def __init__(self, id, brand, model, price, fuel, available):
        self.id = id
        self.brand = brand
        self.model = model
        self.price = price
        self.fuel = fuel
        self.available = available


class Equipment:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
