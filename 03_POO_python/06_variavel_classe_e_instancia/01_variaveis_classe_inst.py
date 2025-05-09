class Estudante:
    escola = "DIO"    #ATRIBUTO DE CLASSE -> IGUAL PARA TODAS AS INSTANCIAS

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.escola}"

def mostrar_valores(*objts):
    for obj in objts:
        print(obj)

gui = Estudante("Guilherme", 56451) #ATRIBUTOS DE INSTANCIA SÃO DEFINIDOS AO INSTANCIAR O OBJETO (NESSE CASO NOME E NUMERO)
gi = Estudante("Giovana", 33543)
mostrar_valores(gui,gi)


print("=======ALTERANDO========")
Estudante.escola = "Python"
jorge = Estudante("Jorge", 16441) #ATRIBUTOS DE INSTANCIA SÃO DEFINIDOS AO INSTANCIAR O OBJETO (NESSE CASO NOME E NUMERO)
maria = Estudante("Maria", 35563)


mostrar_valores(jorge,maria,gui,gi)