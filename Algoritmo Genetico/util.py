from random import randint

class Util:
    """
    Utility class
    """
    def gerar_palavras(n):
        letras = 'abcdefghijklmnopqrstuvxwayz'
        palavra = ''
        for _ in range(n):
            palavra += letras[randint(0,len(letras))]
        return palavra