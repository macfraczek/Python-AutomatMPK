from tkinter import *
from tkinter import ttk
from monety import *

class GUI():
    def __init__(self):
        window = Tk()
        window.title("Automat MPK")

        mainframe = ttk.Frame(window)

        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Automat MPK", font=("Arial", 24, "italic"), foreground="RED").grid(column=1, row=0)

        ttk.Button(mainframe, text="Bilet normalny 20 min", command=lambda : ticket.add(1)).grid(column=0, row=1)
        ttk.Button(mainframe, text="Bilet normalny 40 min", command=lambda: ticket.add(2)).grid(column=1, row=1)
        ttk.Button(mainframe, text="Bilet normalny 60 min", command=lambda: ticket.add(3)).grid(column=2, row=1)
        ttk.Button(mainframe, text="Bilet ulgowy 20 min", command=lambda: ticket.add(4)).grid(column=0, row=2)
        ttk.Button(mainframe, text="Bilet ulgowy 40 min", command=lambda: ticket.add(5)).grid(column=1, row=2)
        ttk.Button(mainframe, text="Bilet ulgowy 60 min", command=lambda: ticket.add(6)).grid(column=2, row=2)
        ttk.Label(mainframe).grid(row=3)
        ttk.Button(mainframe, text="CENNIK",
                   command=lambda: self.showTicketPrize()).grid(column=0,row=4)
        ttk.Button(mainframe, text="Pokaż zakupione bilety", command=lambda: self.showTicket()).grid(column=0, row=5)
        ttk.Button(mainframe, text="Reset zakupionych biletów", command=lambda: ticket.reset()).grid(column=0, row=6)
        ttk.Button(mainframe, text="Zapłać za bilety ", command=lambda: self.payment()).grid(column=0, row=7)
        ttk.Label(mainframe,text="Podaj ilosc biletów", foreground="RED").grid(column=2,row=4)
        e = Entry(mainframe)
        e.grid(column=2, row=5)
        ttk.Button(mainframe, text="Wprowadz", command=lambda : ticket.moreItem(e.get()) ).grid(column=2,row=6)
        ttk.Button(mainframe, text="Monety w automacie", command=lambda : self.showMoney(moneyBox) ).grid(column=1,row=7)



        window.mainloop()
    def showTicket(self):
        windowTicket = Tk()
        windowTicket.title("Zakupione bilety")
        mainframe = ttk.Frame(windowTicket)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=ticket.showTicketWindow(), font=("Arial", 20, "italic"), foreground="BLACK", background="WHITE" ).grid(column=1, row=0)
        ttk.Button(mainframe, text="Close", command=lambda: windowTicket.destroy()).grid(column=1, row=1)
    def showTicketPrize(self):
        windowTicket = Tk()
        windowTicket.title("Cennik")
        mainframe = ttk.Frame(windowTicket)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=ticket.showTicketPrizeWindow(), font=("Arial", 20, "italic"), foreground="BLACK", background="WHITE" ).grid(column=1, row=0)
        ttk.Button(mainframe, text="Close", command=lambda: windowTicket.destroy()).grid(column=1, row=1)
    def payment(self):
        windowPayment = Tk()
        windowPayment.title("Płatność")

        mainframe = ttk.Frame(windowPayment)

        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))

        ttk.Button(mainframe, text="1 gr", command=lambda : tempMoneyBox.add(1)).grid(column=1, row=1)
        ttk.Button(mainframe, text="2 gr", command=lambda : tempMoneyBox.add(2)).grid(column=1, row=2)
        ttk.Button(mainframe, text="5 gr", command=lambda : tempMoneyBox.add(5)).grid(column=1, row=3)
        ttk.Button(mainframe, text="10 gr", command=lambda : tempMoneyBox.add(10)).grid(column=2, row=1)
        ttk.Button(mainframe, text="20 gr", command=lambda : tempMoneyBox.add(20)).grid(column=2, row=2)
        ttk.Button(mainframe, text="50 gr", command=lambda : tempMoneyBox.add(50)).grid(column=2, row=3)
        ttk.Button(mainframe, text="1 zl", command=lambda : tempMoneyBox.add(100)).grid(column=3, row=1)
        ttk.Button(mainframe, text="2 zl", command=lambda : tempMoneyBox.add(200)).grid(column=3, row=2)
        ttk.Button(mainframe, text="5 zl", command=lambda : tempMoneyBox.add(500)).grid(column=3, row=3)
        ttk.Label(mainframe,text="Podaj ilosc monet", foreground="RED").grid(column=4,row=4)
        e = Entry(mainframe)
        e.grid(column=4, row=5)
        ttk.Button(mainframe, text="Wprowadz ilość", command=lambda : tempMoneyBox.moreItem(e.get()) ).grid(column=4,row=6)
        ttk.Button(mainframe, text="Pokaz wprowadzone monety", command=lambda : self.showMoney(tempMoneyBox) ).grid(column=4,row=8)
        ttk.Button(mainframe, text="Płać", command=lambda : self.inputMoney()).grid(column=2,row=8)


        Label(mainframe).grid(column=3)
        Label(mainframe,text='       ').grid(column=0,row=0)
        Label(mainframe).grid(column=5)
    def showMoney(self,moneyWhere):
        windowNew = Tk()
        windowNew.title("Wrzucone monety")
        mainframe = ttk.Frame(windowNew)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
        ttk.Label(mainframe, text=moneyWhere.showMoneyWindow(), font=("Arial", 20, "italic"), foreground="BLACK", background="WHITE" ).grid(column=1, row=0)
        ttk.Button(mainframe, text="Close", command=lambda: windowNew.destroy()).grid(column=1, row=1)
    def inputMoney(self):
        windowNew = Tk()
        windowNew.title("")
        mainframe = ttk.Frame(windowNew)
        mainframe.grid(column=1, row=1, sticky=(N, W, E, S))

        ttk.Label(mainframe, text="Zapłaciłeś   ", foreground="BLACK",font=("Arial", 20, "italic")).grid(column=1, row=1)
        ttk.Label(mainframe, text=tempMoneyBox.returnSum()/100, foreground="BLACK",font=("Arial", 20, "italic")).grid(column=2, row=1)
        ttk.Label(mainframe, text="Wartość biletów", foreground="BLACK",font=("Arial", 20, "italic")).grid(column=1, row=2)
        ttk.Label(mainframe, text=(ticket.countCost()/100), foreground="BLACK",font=("Arial", 20, "italic")).grid(column=2, row=2)
        ttk.Label(mainframe, text="Reszta", foreground="BLACK",font=("Arial", 20, "italic")).grid(column=1, row=3)
        ttk.Label(mainframe, text=(moneyBox.calculateRest(tempMoneyBox,ticket.countCost())), foreground="BLACK",font=("Arial", 20, "italic")).grid(column=2, row=3)


        Label(mainframe,text="     ").grid(column=0,row=0)
        # ttk.Button(mainframe, text="Close", command=lambda: windowNew.destroy()).grid(column=3, row=1)
