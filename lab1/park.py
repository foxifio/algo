class Park:

    def __init__(self, address, length, price):
        self.address = address
        self.length = length
        self.price = price

    def __repr__(self):
        return self.address+" "+str(self.length)+" "+str(self.price)+" \n "
