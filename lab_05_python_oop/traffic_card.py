balance = 0


def charge(amount):
    global balance
    balance += amount


def pay(amount):
    global balance
    balance -= amount


def check():
    global balance
    return balance
