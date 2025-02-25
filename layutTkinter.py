from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1 = Label(i,text='Label 1',bg="yellow")
lb1.place(x=230,y=200)

lb2 = Label(i,text='Label 1',bg="pink")
lb2.place(x=230,y=200)

lb3 = Label(i,text='Label 1',bg="green")
lb3.place(x=230,y=200)

lb4 = Label(i,text='Label 1',bg="red")
lb4.place(x=230,y=200)

"""lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()"""


"""#o codigo abaixo e responsavel posisionar o label no topo da interface
lb1.pack(side="top")
#o codigo abaixo por posicionar o label a esquerda da tela
lb2.pack(side="left")
#o codigo abaixo por posicionar o label a direita da tela
lb3.pack(side="right")
#o codigo abaixo por posicionar o label a baixo da tela
lb4.pack(side="bottom")"""

lb1.pack(side='left')
lb2.pack(side='left')
lb3.pack()
lb4.pack()

i.mainloop()