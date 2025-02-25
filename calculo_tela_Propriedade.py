from tkinter import *

def bt_soma():
    #o codigo abaixo e para validar a entrada apenas de numero
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        #se os valores nao forem numericos imprime a mensagem abaixo
        lb["text"] = num1 + num2
        lb["bg"]= "#00FA9A"
    else:
        lb["text"] = "valores sao invalidos"
        lb["bg"] = "red"

def bt_subtração():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 - num2
        lb["bg"]= "#00FA9A"
    else:
        lb["text"] = "valores sao invalidos"
        lb["bg"] = "red"

def bt_multiplicacao():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 * num2
        lb["bg"]= "#00FA9A"
    else:
        lb["text"] = "valores sao invalidos"
        lb["bg"] = "red"

def bt_divisao():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb["text"] = num1 / num2
        lb["bg"]= "#00FA9A"
    else:
        lb["text"] = "valores sao invalidos"
        lb["bg"] = "red"

i=Tk()
i.title("Programa Financeiro")
i.geometry('980x720+250+30')

lb=Label(i,text="0")
lb.place(x=230,y=200)

bt=Button(i,width="20",text='calcular +',command=bt_soma)
bt.place(x=230,y=230)

bt=Button(i,width="20",text='calcular -',command=bt_subtração)
bt.place(x=230,y=260)

bt=Button(i,width="20",text='calcular *',command=bt_multiplicacao)
bt.place(x=385,y=230)

bt=Button(i,width="20",text='calcular /',command=bt_divisao)
bt.place(x=385,y=260)

ed1 = Entry(i)
ed1.place(x=230,y=150)

ed2 = Entry(i)
ed2.place(x=230,y=180)

lb=Label(i,text="CaioLuizBattisti")
lb.place(x=230,y=200)
i.mainloop()