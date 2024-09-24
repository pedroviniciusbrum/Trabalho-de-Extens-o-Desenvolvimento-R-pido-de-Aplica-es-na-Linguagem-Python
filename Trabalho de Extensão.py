from tkinter import *
from tkinter import ttk

ped = open("./pedidos.txt", "a")

Requerentes = []

for line in ped.readlines():
    Requerentes.append(line)

class Requerente:
    def __init__(self, nome, data, chegou, pegou):
        self.Nome = nome
        self.Data = data
        self.Chegou = chegou
        self.Pegou = pegou

class Hub:
    def addreq(req):
        Requerentes.append(req)

root = Tk()

root.title("Certidões")

root.geometry('860x600')
#====================================================================================================
#==========================================Tela de Inicio============================================
#====================================================================================================
lbl = Label(root, text="Pesquisar Pedido: ")
lbl.grid(column=0, row=0)
inh = Entry(root, width=25)
inh.grid(column=1, row=0)

def register():
    root2 = Tk()
    root2.title("Cadastrar Certidões")
    root2.geometry('860x600')

    lbl1 = Label(root2, text="Nome_Completo: ")
    lbl1.grid(column=0, row=0)
    in1 = Entry(root2, width=25)
    in1.grid(column=1, row=0)

    lbl2 = Label(root2, text="Data(ddMMyyyy): ")
    lbl2.grid(column=0, row=1)
    in2 = Entry(root2, width=25)
    in2.grid(column=1, row=1)

    def clicked(): 
        req = Requerente(in1.get(),in2.get(), 0, 0)
        hub1 = Hub
        hub1.addreq(req)
        linerow = '"' + in1.get() + '"' + " " + in2.get() + " " + "0" + " " + "0" + ";"
        ped.write("\n" + linerow)
        ped.close()
        print(Requerentes[0].Nome)
        print(Requerentes[0].Data)

    btn = Button(root, text="Cadastrar Pedido", command=clicked)
    btn.grid(column=1, row=2)

btn = Button(root, text="Cadastrar Novo Pedido", command=register)
btn.grid(column=1, row=0)

#====================================================================================================
#========================================Tela de Cadastro============================================
#====================================================================================================

lbl1 = Label(root, text="Nome_Completo: ")
lbl1.grid(column=0, row=0)
in1 = Entry(root, width=25)
in1.grid(column=1, row=0)

lbl2 = Label(root, text="Data(ddMMyyyy): ")
lbl2.grid(column=0, row=1)
in2 = Entry(root, width=25)
in2.grid(column=1, row=1)

def clicked(): 
   req = Requerente(in1.get(),in2.get(), 0, 0)
   hub1 = Hub
   hub1.addreq(req)
   linerow = '"' + in1.get() + '"' + " " + in2.get() + " " + "0" + " " + "0" + ";"
   ped.write("\n" + linerow)
   ped.close()
   print(Requerentes[0].Nome)
   print(Requerentes[0].Data)

btn = Button(root, text="Cadastrar Pedido", command=clicked)
btn.grid(column=1, row=2)

#====================================================================================================
#====================================================================================================
#====================================================================================================

root.mainloop()



