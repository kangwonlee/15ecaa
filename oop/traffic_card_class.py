class TrafficCardClass(object):
    def __init__(self):
        self.balance = 0

    def charge(self, amount):
        self.balance += amount

    def pay(self, amount):
        self.balance -= amount

    def check(self):
        return self.balance

if "__main__" == __name__:
    my_card = TrafficCardClass()
    print "my_card.check() =", my_card.check()
    print "my_card.charge(10000) =", my_card.charge(10000)
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()

    your_card = TrafficCardClass()
    print "your_card.check() =", your_card.check()
