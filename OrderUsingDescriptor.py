from grr.uddhav_test.PriceDescriptor import PriceDescriptor
from grr.uddhav_test.QuantityDescriptor import QuantityDescriptor


class Order(object):
    price = PriceDescriptor()
    quantity = QuantityDescriptor()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


if __name__ == "__main__":
    apple_order = Order('apple', -5, 10)
    print(apple_order.total())
