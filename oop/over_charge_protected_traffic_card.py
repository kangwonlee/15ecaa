import traffic_card_class as tcc
# because name is traffic_card_class too long, use as "tcc" instead


# make NoOverChargeCard based on tcc.TrafficCardClass : inheritance
# class TrafficCardClass is in tcc == traffic_card_class.py
class NoOverChargeCard(tcc.TrafficCardClass):
    def pay(self, amount):
        # "override" pay() "method" of TrafficCardClass
        if 0 > (self.balance - amount):
            print "error : not enough balance"
            self.balance = 0
        else:
            self.balance -= amount

if "__main__" == __name__:
    my_card = NoOverChargeCard()
    print "my_card.check() =", my_card.check()
    print "my_card.charge(10000) =", my_card.charge(10000)
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()

    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
    print "my_card.pay(1250) =", my_card.pay(1250)
    print "my_card.check() =", my_card.check()
