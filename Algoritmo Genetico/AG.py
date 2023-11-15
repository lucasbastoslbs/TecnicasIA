from random import randint

from cromossomo import Cromossomo
from util import Util

class AG:
	def gerar_populacao(populacao:list[Cromossomo], tamanho:int, estado_final:str) -> None:
		"""Método de classe que gera a 1a população totalmente aleatória

		Args:
			populacao (list[Cromossomo]): lista para individuos gerados
			tamanho (int): quantos indivíduos/estados se quer colocar na lista
			estado_final (str): palavra/valor desejado
		"""
		util = Util()
		for i in range(tamanho):
			populacao.append(Cromossomo(util.gerar_palavras(len(estado_final)), estado_final))

	def exibir(populacao:list[Cromossomo]) -> None:
		"""Método de classe que ordena uma lista contendo Cromossomos/Estados/Indivíduos

		Args:
			populacao (list): lista contendo todos os cromossomos/indivíduos/estados
		"""
		for i in populacao:
			print(i)

	def selecionar_por_torneio(populacao:list[Cromossomo], nova_populacao:list[Cromossomo], taxa_selecao:int) -> None:
		"""Método de classe que seleciona elementos/cromossomos/indivíduos para a novaPopulacao a partir do algoritmo de sorteio

		Args:
			populacao (list[Cromossomo]): lista com os Cromossomos da população atual
			nova_populacao (list[Cromossomo]): lista para os Cromossomos selecionados
			taxa_selecao (int): porcentagem (sobre 100) de quantos serão selecionados
		"""
		qtd_selecionados = int(taxa_selecao * len(populacao)/100)
		nova_populacao.append(populacao[0])
		i = 0
		while i <= qtd_selecionados:
			torneio = []
			tam = len(populacao)-1
			c1,c2,c3 = populacao[randint(0,tam)],populacao[randint(0,tam)],populacao[randint(0,tam)]
			while c2 == c1:
				c2 = populacao[randint(0,tam)]
			while c3 == c2 or c3 == c1:
				c3 = populacao[randint(0,tam)]
			torneio.append(c1)
			torneio.append(c2)
			torneio.append(c3)
			torneio = sorted(torneio)

			selecionado = torneio[0]

			if not selecionado in nova_populacao:
				nova_populacao.append(selecionado)
				i+=1

	def selecionar_por_roleta(populacao:list[Cromossomo], nova_populacao:list[Cromossomo], taxa_selecao: int) -> None:
		"""Método de classe que seleciona elementos/cromossomos/indivíduos para a novaPopulacao a partir do algoritmo da roleta

		Args:
			populacao (list[Cromossomo]): lista com os Cromossomos da população atual
			nova_populacao (list[Cromossomo]): lista para os Cromossomos selecionados
			taxa_selecao (int): porcentagem (sobre 100) de quantos serão selecionados
		"""
		aptidao_total = 0
		for i in populacao:
			aptidao_total += i.aptidao
		
		for i in populacao:
			i.porcentagem_aptidao = int(i.aptidao * 100 / aptidao_total)
			if i.porcentagem_aptidao == 0:
				i.porcentagem_aptidao = 1
			
		sorteio = []
		for i in populacao:
			for _ in range(i.porcentagem_aptidao):
				sorteio.append(i)

		qtd_selecionados = taxa_selecao * len(populacao) / 100
		nova_populacao.append(populacao[0])
		i = 1
		while i <= qtd_selecionados:
			posicao_sorteio = randint(0,len(sorteio)-1)
			try:
				selecionado = sorteio[posicao_sorteio]
				nova_populacao.append(selecionado)
				while sorteio.remove(selecionado):
					pass
			except:
				print('Tentou pegar uma posição inválida do sorteio')
			i+=1
		
	def reproduzir(populacao:list[Cromossomo], nova_populacao:list[Cromossomo], taxa_reproducao: int, estado_final:str) -> None:
		"""Método de classe que seleciona elementos/cromossomos/indivíduos para a novaPopulacao a partir do algoritmo de sorteio

		Args:
			populacao (list[Cromossomo]): lista com os cromossomos vigentes
			nova_populacao (list[Cromossomo]): lista para os cromossomos gerados no cruzamento entre pai e uma mae
			taxa_reproducao (int): porcentagem (sobre 100) de quantos serão reproduzidos/criados/gerados
			estado_final (str): palavra desejada que é utilizada para calcular a aptidão dos cromossomos gerados
		"""
		qtd_reproduzidos = taxa_reproducao * len(populacao) / 100
		i = 0
		while i < qtd_reproduzidos:
			tam = len(populacao)-1
			pai,mae = populacao[randint(0,tam)],populacao[randint(0,tam)]
			while mae == pai:
				mae = populacao[randint(0,tam)]

			meio = int(len(pai.valor)/2)
			s_filho1 = pai.valor[:meio] + mae.valor[meio:]
			s_filho2 = mae.valor[:meio] + pai.valor[meio:]
			# print('cruzou')
			# print('pai: ',pai.valor[:meio],'Mae',mae.valor[meio:])
			# print(s_filho1)
			# print(s_filho2)

			nova_populacao.append(Cromossomo(s_filho1,estado_final))
			nova_populacao.append(Cromossomo(s_filho2,estado_final))

			i += 2
		while(len(nova_populacao) > len(populacao)):
			nova_populacao.pop()

	def mutar(populacao:list[Cromossomo], estado_final:str) -> None:
		"""Método de classe com a função de esporadicamente mutar elementos da populacao passada no parametro

		Args:
			populacao (list[Cromossomo]): lista de cromossomos vigentes
			estado_final (str): palavra desejada, em que é utilizada para recalcular a aptidão dos cromossomos mutados
		"""
		qtd_mutantes = randint(0,int(len(populacao) / 5))
		util = Util()
		for _ in range(qtd_mutantes):
			posicao_mutante = randint(0, len(populacao)-1)
			mutante = populacao[posicao_mutante]
			valor_mutado = mutante.valor
			caracter_mutante = valor_mutado[randint(0,len(valor_mutado)-1)]
			caracter_sorteado = util.letras[randint(0,util.tamanho-1)]
			valor_mutado = valor_mutado.replace(caracter_mutante,caracter_sorteado)
			print('Vai mutar', mutante)
			mutante = Cromossomo(valor_mutado,estado_final)
			print('Mutado ', mutante)
			populacao[posicao_mutante] = mutante
