from tkinter import *
i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

'''lb1=Label(i,text="Login:",bg="yellow")
#componente .grid serve tambem para posicionar utilizando indicativo de linha(row) e coluna (column).

lb1.grid(row=1,column=1)

lb2=Label(i,text="Senha:",bg="red")
lb2.grid(row=9,column=1)

ed1 = Entry(i)
ed1.grid(row=3,column=1)

ed2 = Entry(i)
ed2.grid(row=10,column=1)

bt1 = Button(i,text="Login")
bt1.grid(row=11,column=1)'''

#o codigo abaixo faz coreção das posições das labels,caixa de texto e botao [✓] Feito
lb1=Label(i,text="Login:",bg="yellow")
lb1.place(x=800,y=1)

lb2=Label(i,text="Senha:",bg="red")
lb2.place(x=800,y=23)

ed1 = Entry(i)
ed1.place(x=842,y=23)

ed2 = Entry(i)
ed2.place(x=842,y=4)

bt1 = Button(i,text="Login")
bt1.place(x=800,y=43)

i.mainloop()