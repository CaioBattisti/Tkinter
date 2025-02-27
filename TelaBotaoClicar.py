from tkinter import *

#criando uma função para clique no botão
def bt_click():
    # o label que usa propriedade TEXT recebera a mensagem "trocou o texto"
    lb["text"]="trocou o texto"
    #esse print abaixo exibe o texto na tela do console.
    print("O botão foi clicado!")

def bt_clicar():
    #esse print exibe  texto digitao o texto digitado na caixa e exibe na  label da tela
    print(ed.get())
    lb['text']=ed.get()

# i (instanciar) recebe o objeto Tk
i=Tk()
#gerar titulo da janela
i.title('Programa Financeiro')
i.geometry('980x720+250+30')
i['bg']="green"

#i.wm_iconbitmap('icone.ico')
lb = Label(i,text='Nome do Usuario')
lb.place(x=100,y=100)

bt = Button(i,width="20",text='OK',command=bt_click)
bt.place(x=230,y=100)
#o codigo abaixo cria um botao e posiciona abaixo do botao OK
bt = Button(i,width="20",text='capturar',command=bt_clicar)
bt.place(x=230,y=190)

#CRIA A CAIXA DE TEXTO PARA DIGITAR ALGO DENTRO
ed=Entry(i)
ed.place(x=230,y=150)
i.mainloop() 