#exercicio1
from tkinter import *
class Janela:
    def __init__(self, instancia_de_Tk):
        principal = Menu(instancia_de_Tk)
        arquivo =Menu(principal)
        arquivo.add_command(Label="Abrir",command=self.abrir)
        arquivo.add_command(Label="Salvar",command=self.salvar)
        principal.add_command(Label="Arquivo",command=self.arquivo)
        principal.add_command(Label="Ajuda",command=self.ajuda)
        instancia_de_Tk.config(menu=principal)
    def abrir(self):
        print("abrir")
    def salvar(self):
        print("Salvar")
    def ajuda(self):
        print("Ajuda")

raiz =Tk()
Janela(raiz)
raiz.mainloop()