from weakref import WeakKeyDictionary


class QuantityDescriptor(object):
    def __init__(self):
        self._quantity = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self._quantity.get(instance)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("quantity must not be negative!")

    def __delete__(self, instance):
        del self._quantity[instance]
