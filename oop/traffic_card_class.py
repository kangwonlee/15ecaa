# make TrafficCardClass based on another class named "object"
class TrafficCardClass(object):
    def __init__(self):
        self.balance = 0

    def charge(self, amount):
        self.balance += amount
        # no return value -> None

    def pay(self, amount):
        self.balance -= amount

    def check(self):
        return self.balance


print("__name__ in traffic_card_class.py =", __name__)
if "__main__" == __name__:
    # do not run below if this file is being imported
    my_card = TrafficCardClass()
    # no direct access to my_card.balance : encapsulation
    print("my_card.check() =", my_card.check())
    print("my_card.charge(10000) =", my_card.charge(10000))
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())

    your_card = TrafficCardClass()
    print("your_card.check() =", your_card.check())

    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
    print("my_card.pay(1250) =", my_card.pay(1250))
    print("my_card.check() =", my_card.check())
