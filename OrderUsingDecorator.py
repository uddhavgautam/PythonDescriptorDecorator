from grr.uddhav_test.PriceDecorator import PriceDecorator
from grr.uddhav_test.QuantityDecorator import QuantityDecorator


class Order(object):

    def __init__(self, name, price, quantity):
        self.name = name

        priceDecorator = PriceDecorator(price)
        self.price = priceDecorator.price

        quantityDecorator = QuantityDecorator(quantity)
        self.quantity = quantityDecorator.quantity

    def total(self):
        return self.price * self.quantity


if __name__ == "__main__":
    apple_order = Order('apple', 5, 10)
    print(apple_order.total())
