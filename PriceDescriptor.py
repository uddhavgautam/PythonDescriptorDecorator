from weakref import WeakKeyDictionary


class PriceDescriptor(object):
    def __init__(self):
        self._price = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._price.get(instance)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("price must not be negative!")

    def __delete__(self, instance):
        del self._price[instance]
