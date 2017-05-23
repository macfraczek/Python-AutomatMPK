from Ticket import *


class UnkownCoinException(Exception):
    def __init__(self,temp):
        super().__init__("Unkown coin '{}'".format(temp))
        print("Unkown coin '{}'".format(temp))

class Coin():
    availableCoins=(1,2,5,10,20,50,100,200,500)
    _value=0
    def __init__ (self, value):
        if value in self.availableCoins:
            self._value = value
        else:
            try:
                raise UnkownCoinException(value)
            except UnkownCoinException:
                pass
    def returnValue(self):
        return self._value
    def check(self):
        if self._value in self.availableCoins:
            return True
        else:
            return False

class MoneyBox(Item):
    def __init__(self):
        self._dict={x: 0 for x in Coin.availableCoins}
        self._counter = 1
    def add(self, coin):
        coin=Coin(coin)
        if isinstance(coin, Coin) and coin.check():
            for i in range(self._counter):
                self._dict[coin.returnValue()]=1+self._dict[coin.returnValue()]
        self._counter=1
    def returnSum(self):
        sum=0.00
        for k, v in self._dict.items():
            sum += k*v
        return sum
    def setZero(self):
        for k, v in self._dict.items():
            self._dict[k] = 0
    def setAmmount(self,ammount):
        try:
            if ammount<0:
                raise BadAmmountException()
            if (ammount%1):
                raise BadAmmountException()
        except:
            pass
        else:
            for k, v in self._dict.items():
                self._dict[k] = ammount
    def showMoneyWindow(self):
            string=""
            for x in Coin.availableCoins:
                string += str(x/100)
                if x >=10 :
                    string+="0"
                string += "\t"
                string += str(self._dict[x])
                string +="\n"
            return string
    def addMoneyTrans(self,temp):
        for k, v in self._dict.items():
            self._dict[k]+=temp._dict[k]
    def calculateRest(self,b,ticketCost):
        """
        self - automat, b - wprowadzone monety
        """
        inputMoney = b.returnSum()

        if (inputMoney < ticketCost):
            return "To za mało"

        rest = inputMoney - ticketCost
        if rest == 0:
            self.addMoneyTrans(b)
            ticket.reset()
            return "Brak reszty"

        tempB=MoneyBox()
        tempS=MoneyBox()
        for k, v in tempB._dict.items():
            tempB._dict[k]=b._dict[k]
            tempS._dict[k]=self._dict[k]

        self.addMoneyTrans(b)
        b.setZero()
        counterLoop=4
        while ((inputMoney-ticketCost) and (counterLoop) and (b.returnSum() != rest)):
            counterLoop-=1
            print(counterLoop)
            for i in  (500,200,100,50,20,10,5,2,1):
                for j in range(10):
                    if (self._dict[i]>0) and (i+b.returnSum() <= rest):
                        self._dict[i] -=1
                        b._dict[i] +=1
                        print(i)

        if rest == b.returnSum():
            ticket.reset()
            return b.showMoneyWindow()
        else:
            for k, v in tempB._dict.items():
                b._dict[k] = tempB._dict[k]
                self._dict[k] = tempS._dict[k]
            return "Nie można wydać reszty"


moneyBox=MoneyBox()
moneyBox.setAmmount(100)

tempMoneyBox=MoneyBox()