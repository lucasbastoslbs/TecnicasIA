from util import Util

from AG import AG

util = Util()

tamanho_populacao = 1000
estado_final = 'teclado'
#20-40
taxa_selecao = 30
#5-10
taxa_mutacao = 5
qtd_geracao = 50

populacao = []
nova_populacao = []
AG.gerar_populacao(populacao,tamanho_populacao,estado_final)
populacao = sorted(populacao)
print('Geracao 1')
AG.exibir(populacao)
for i in range(qtd_geracao):
    #AG.selecionar_por_torneio(populacao,nova_populacao,taxa_selecao)
    AG.selecionar_por_roleta(populacao,nova_populacao,taxa_selecao)
    AG.reproduzir(populacao,nova_populacao,100-taxa_selecao,estado_final)

    if i % (len(populacao) / taxa_mutacao) == 0:
        AG.mutar(nova_populacao,estado_final)

    populacao = []
    #metodo criado para evitar mesma posicao de memoria
    populacao = util.copiar(nova_populacao)
    nova_populacao = []
    populacao = sorted(populacao)
    print('\n\n Geracao',i)
    AG.exibir(populacao)