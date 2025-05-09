#Atributos publicos e privados
#Como em python não temos uma palavra reservada para definir se é publico ou privado usamos convenções
#PUBLICO -> nome_atributo
#PRIVADO -> _nome_atributo
#note que para atributos privados deve começar com "_"

class Conta:
    def __init__(self, nro_agencia ,saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
    
    def depositar(self, valor):
        self._saldo += valor
    
    def sacar(self, valor):
        self._saldo -= valor
    
    #não é utilizado get em python, no exemplo 02 e 03 temos como fazer isso em python
    def get_saldo(self):
        return self._saldo


conta = Conta("0001", 100)

print(conta.nro_agencia)
print(conta.get_saldo())
