# -*- coding: utf8 -*-
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


print "__name__ in over_charge_protected_traffic_card.py =", __name__
if "__main__" == __name__:
    # do not run below if this file is being imported

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
