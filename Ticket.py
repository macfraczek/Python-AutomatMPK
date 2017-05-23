class BadAmmountException(Exception):
    def __init__(self):
        super().__init__("Input only positive integer !")
        print("Input only positive integer !")

class Item():
    def moreItem(self,value):
        value = int(value)
        try:
            if (value<0):
                raise BadAmmountException()
            if (value%1):
                raise BadAmmountException()
        except:
                pass
        else:
            self._counter=value


class Ticket(Item):
    def __init__(self):
        self._ticketDict={1:0,2:0,3:0,4:0,5:0,6:0}
        self._ticketID={1:"Normalny 20min",2:"Normalny 40min",3:"Normalny 60min",4:"Ulgowy 20min",5:"Ulgowy 40min",6:"Ulgowy 60min"}
        self._ticketCost={1:300,2:480,3:600,4:150,5:240,6:300}
        self._counter=1
    def showTicket(self):
            for x in range(1,7):
                print(self._ticketID[x],"\t",self._ticketDict[x])
    def showTicketWindow(self):
            string=""
            for x in range(1,7):
                string += str(self._ticketID[x])
                string += "\t"
                string += str(self._ticketDict[x])
                string +="\n"
            return string
    def showTicketPrizeWindow(self):
            string=""
            for x in range(1,7):
                string += str(self._ticketID[x])
                string += "\t"
                string += str(self._ticketCost[x]/100)+"0"
                string +="\n"
            return string
    def add(self,value):
         if value in self._ticketDict:
             for i in range(self._counter):
                self._ticketDict[value]=1+self._ticketDict[value]
         else:
             print("Wrong ticket")
         self._counter = 1
    def countCost(self):
        cost = 0.0
        for x in range(1, 7):
            cost = cost + self._ticketDict[x] * self._ticketCost[x]
        return cost
    def reset(self):
        for x in range(1, 7):
            self._ticketDict[x]=0


ticket=Ticket()