'''
INTERFACES DEINEM O QUE UMA CLASSE DEVE FAZER E NÃO COMO
DECLARA UM MÉTODO (O QUE DEVE SER FEITO) E SUAS ASSINATURAS
    EM PYTHON UTILIZAMOS CLASSES ABSTRATAS PARA DEFINI-LAS
    CLASSES ABSTRATAS NAO PODEM SER INSTANCIADAS

PYTHON NÃO FORNECE CLASSES ABSTRATAS MAS VEM COM UM MODULO ABC PARA DEFINIR
'''
from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    #Método abstrato nao tem um corpo mas as classes filhas devem implementar
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV")

    def desligar(self):
        print("Desligando TV...")
    
    @property
    def marca(self):
        return "TV SAMSUNG 55 POLEGADAS"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando AR Condicionado")

    def desligar(self):
        print("Desligando AR Condicionado...")

    @property
    def marca(self):
        return "AR LG DUAL INVERTER 9000 BTUS"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

ar = ControleArCondicionado()
ar.ligar()
ar.desligar()
print(ar.marca)
