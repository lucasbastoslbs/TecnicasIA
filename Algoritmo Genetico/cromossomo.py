class Cromossomo:
    """
    Classe que representa um estado ou indivíduo de um problema para o AG
    """
    valor : str
    aptidao : int
    def __init__(self,valor,estado_final):
        """
        Construtor que recebe um valor/palavra qualquer e a palavra final, calculando o fitness desse indivíduo (valor/palavra)
        param valor:str palavra,valor ou estado do indivíduo
        param estado_final:str palavra ou valor ou indivíduo que se deseja gerar
        """
        self.valor = valor
        self.aptidao = self.calcular_aptidao(estado_final)

    def calcular_aptidao(self, estado_final : str) -> int:
        """Método que recebe um estado/indivíduo e retorna sua aptidão, ou seja, quão próximo o estado está da solução

        Args:
            estado_final (str): palavra ou valor ou indivíduo que se deseja gerar

        Returns:
            int: o valor da aptidao do estado
        """
        nota = 0
        for i,v in enumerate(estado_final):
            if v in self.valor:
                nota += 5
            if i == self.valor.index(v):
                nota += 50
        return nota

    def __str__(self):
        return 'Valor: %s - %s' % (self.valor,self.aptidao)

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.valor == other.valor

    def __lt__ (self, other):
        if self.aptidao == other.aptidao:
            return self.b < other.b
        return self.a < other.b

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.a == other.b and self.b == other.b

    def __ne__ (self, other):
        return not self.__eq__(other)

