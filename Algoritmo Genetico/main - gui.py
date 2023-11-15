from AG import AG
from util import Util
from tkinter import *

root = Tk()
root.title('Busca Palavra')

tamanho_populacao = IntVar(value=1000)
estado_final = StringVar(value='teclado')
taxa_selecao = IntVar(value=30)
taxa_mutacao = IntVar(value=5)
qtd_geracao = IntVar(value=50)

# tamanho_populacao = IntVar()
# estado_final = StringVar()
# taxa_selecao = IntVar()
# taxa_reproducao = IntVar()
# taxa_mutacao = IntVar()
# qtd_geracao = IntVar()

def limpar():
    global tamanho_populacao,estado_final,taxa_selecao,taxa_mutacao,qtd_geracao
    tamanho_populacao.set(0)
    estado_final.set('')
    taxa_selecao.set(0)
    taxa_mutacao.set(0)
    qtd_geracao.set(0)

def gerar():
    global tamanho_populacao,estado_final,taxa_selecao,taxa_mutacao,qtd_geracao
    util = Util()
    populacao = []
    nova_populacao = []
    AG.gerar_populacao(populacao,tamanho_populacao.get(),estado_final.get())
    populacao = sorted(populacao)
    print('Geracao 1')
    #AG.exibir(populacao)
    for i in range(qtd_geracao.get()):
        AG.selecionar_por_torneio(populacao,nova_populacao,taxa_selecao.get())
        #AG.selecionar_por_roleta(populacao,nova_populacao,taxa_selecao.get())
        AG.reproduzir(populacao,nova_populacao,100-taxa_selecao.get(),estado_final.get())

        if i % (len(populacao) / taxa_mutacao.get()) == 0:
            AG.mutar(nova_populacao,estado_final.get())

        populacao = []
        #metodo criado para evitar mesma posicao de memoria
        populacao = util.copiar(nova_populacao)
        nova_populacao = []
        populacao = sorted(populacao)
        print('\n\n Geracao',i)
        AG.exibir(populacao)

Label(root,text='Tamanho Populacao:').grid(row=0,column=0)
Entry(root,textvariable=tamanho_populacao).grid(row=0,column=1)

Label(root,text='Estado Final:').grid(row=1,column=0)
Entry(root,textvariable=estado_final).grid(row=1,column=1)

Label(root,text='Taxa Seleção (20-40):').grid(row=2,column=0)
Entry(root,textvariable=taxa_selecao).grid(row=2,column=1)

Label(root,text='Taxa Mutação (5-10):').grid(row=3,column=0)
Entry(root,textvariable=taxa_mutacao).grid(row=3,column=1)

Label(root,text='Qtd Geração:').grid(row=4,column=0)
Entry(root,textvariable=qtd_geracao).grid(row=4,column=1)

Button(root,text='Gerar', command=gerar).grid(row=5,column=0)
Button(root,text='Limpar', command=limpar).grid(row=5,column=1)

root.mainloop()