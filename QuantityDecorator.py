class QuantityDecorator(object):
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, v):
        if (v < 0): raise Exception("quantity must be greater than zero!")
        self._quantity = v
