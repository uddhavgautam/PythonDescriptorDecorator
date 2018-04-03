def validate(instance, price, quantity):
    if price < 0:
        raise Exception("negative price!")
    elif quantity < 0:
        raise Exception("negative quantity!")
    else:
        instance.price = price
        instance._quantity = quantity



class OrderUsingOldWay:
    def __init__(self, name, price, quantity):
        self.name = name
        # validation in constructor
        validate(self, price, quantity)
        self.price = price
        self._quantity = quantity

    def __setPrice__(self, instance, value):
        # validation in setter
        if value < 0:
            raise ValueError("price must not be negative!")
        self.price = value

    def __setQuantity__(self, instance, value):
        #validation in setter
        if value < 0:
            raise ValueError("price must not be negative!")
        self._quantity = value

    def total(self):
        return self.price * self._quantity


if __name__ == "__main__":
    apple_order = OrderUsingOldWay('apple', 5, 10)
    apple_order.__setPrice__(apple_order, 23)
    apple_order.__setQuantity__(None, 23)
    print(apple_order.total())
