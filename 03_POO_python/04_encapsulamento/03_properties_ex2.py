from datetime import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = datetime.now().year
        return _ano_atual - self._ano_nascimento
    #É POSSÍVEL FAZER OS GETTERS E SETTERS PORÉM NO PYTHON É MUITO MAIS UTILIZADO DESSA MANEIRA (USANDO PROPERTIES)

pessoa = Pessoa("Mateus", 2003)

print(pessoa.nome)
print(pessoa.idade)
