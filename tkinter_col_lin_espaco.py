from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')
lb3=Label(i,text="")
lb3.grid(row=0,column=0)

lb4=Label(i,text="")#dando espaço
lb4.grid(row=0,column=0)

lb1=Label(i,text="Login:",bg="yellow")
lb1.grid(row=1,column=1)

lb5=Label(i,text="")#dando espaço
lb5.grid(row=2,column=0)

lb2=Label(i,text="Senha:",bg="red")
lb2.grid(row=3,column=1)

ed1 = Entry(i)
ed1.grid(row=1,column=2)

ed2 = Entry(i)
ed2.grid(row=3,column=2)

lb6=Label(i,text="")#dando espaço
lb6.grid(row=4,column=0)

bt1 = Button(i,text="Login")
bt1.grid(row=5,column=1)

i.mainloop()