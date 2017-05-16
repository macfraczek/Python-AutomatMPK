class Coin:
    _value=0
    def __init__ (self, value):
        if value in (1,2,5):
            self._value = value
        else:
            self._value = 0
    def getValue(self):
        return self._value

class StoringCoins():
    def __init__(self):
        self.list=[]
    def add(self, coin):
        coin=Coin(coin)
        if isinstance(coin, Coin):
            self.list.append(coin)
        else:
            print("Unkown coin")
    def suma(self):
        sum=0
        for i in range (0, len(self.list)):
            sum += self.list[i].getValue()
        return sum
    def giveCoin(self,value):
        for x in self.list:
            if x.getValue()==value:
                self.list.remove(x)
                return value
            else:
                print("No such coin")

class Moneybox():
    def __init__(self):
        self.list=[]
    def add(self, coin):
        coin=Coin(coin)
        if isinstance(coin, Coin):
            self.list.append(coin)
        else:
            print("Unkown coin")
    def suma(self):
        sum=0
        for i in range (0, len(self.list)):
            sum += self.list[i].getValue()
        return sum



a=Coin(5)
print(a.getValue())


b=Moneybox()
b.add(5)
b.add(5)
print(b.suma())


c=StoringCoins()
c.add(5)
c.add(2)
print(c.suma())