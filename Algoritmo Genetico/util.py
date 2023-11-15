from random import randint

class Util:
    """
    Utility class
    """

    def __init__(self):
        self.letras = 'abcdefghijklmnopqrstuvwxyz'
        self.tamanho = len(self.letras)

    def gerar_palavras(self,n:int) -> str:
        palavra = ''
        for _ in range(n):
            palavra += self.letras[randint(0,self.tamanho-1)]
        print(palavra)
        return palavra
    
    def copiar(self, lista:list) -> list:
        return [i for i in lista]