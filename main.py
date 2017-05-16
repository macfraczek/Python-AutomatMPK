
from tkinter import *
from tkinter import ttk
import monety


# Tworzenie okna
window=Tk()
window.title("Skarbonka")

# Tworzenie siatki na przyciski
mainframe=ttk.Frame(window)

# Umieszczenie siatki w oknie
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Dodanie przycisków do wrzucania monet
i=0
#for c in COINS:
# ttk.Button(mainframe, text="Wrzuć "+str(c)+"zł",
# command=lambda c=c: pb.add(Coin(c))).grid(column=2, row=i)
# i+=1

# Dodanie przycisku sprawdzenia wartości zawartości
ttk.Button(mainframe, text="Przerwij",
 command=lambda: print(pb.value()) ).grid(column=1, row=0)


#window.mainloop()