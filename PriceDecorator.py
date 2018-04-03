
class PriceDecorator(object):
    def __init__(self, price):
        self.price = price

    @property  # property decorator
    def price(self):
        return self._price  # note: _price is different than price. If we put price then indefinite recursion happens

    @price.setter
    def price(self, v):
        if (v < 0): raise Exception("price must be greater than zero!")
        self._price = v

