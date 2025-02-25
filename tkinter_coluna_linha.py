from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb1=Label(i,text="Login",bg="yellow")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e coluna (column).
lb1.grid(row=1,column=1000)

lb2=Label(i,text="Senha",bg="red")
lb2.grid(row=9,column=2)

ed1 = Entry(i)
ed1.grid(row=3,column=2)

ed2 = Entry(i)
ed2.grid(row=10,column=2)

bt1 = Button(i,text="Login")
bt1.grid(row=11,column=2)

i.mainloop()