class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instancia da classe")
        

    def latir(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "Amarelo")
c.latir()
del c

criar_cachorro()



