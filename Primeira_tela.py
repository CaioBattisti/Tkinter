#comando baixo importa tudo da biblioteca que e necessaria para a criação de telas. (ASTERISCO significa tudo)
from tkinter import *

#i(INSTRANCIAR) recebe o objeto Tk
i = Tk()

#gerar titolo da janela
i.title('Programa Financeiro')

#Propriedade que altera o tamanho da janela (980x720) e a distancia da dirita e topo da tela (250X30)
i.geometry('980x720+250+30')

#propriedades grficas,cor de fundo da tela (bg) ou (background),nao pode passar o i com ponto! DEVE SER i[]
i['bg']= "yellow"

#cria um icone na janela, VOCE DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO.
# i.wm_iconbitmap('icone.ico')

#cria um label e posiciona (place). ele em relação a tela.
lb = Label(i,text='Nome do Usuario')
lb.place(x=100,y=100)

#cria um botao e posiciona (place) ele em relação a label.
bt =Button(i,width='20',text='OK')
bt.place(x=230,y=100)

#gera a janela grafica
i.mainloop()