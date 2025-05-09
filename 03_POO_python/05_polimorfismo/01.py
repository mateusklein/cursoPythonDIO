'''
Poliformismo significa ter muitas formas
    len("python")
    len([10, 20, 30])
    -> o len é um exemplo dentro da propria linguagem

Polimorfismo com heranca -> mesmo método com comportamento diferente
    -> sobrescrita de método
'''

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

class Bemtevi(Passaro):
    pass

def plano_de_voo(passaro):
    passaro.voar()

pardal = Pardal()
avestruz = Avestruz()
bemtevi = Bemtevi()

plano_de_voo(pardal)
plano_de_voo(avestruz)
plano_de_voo(bemtevi)