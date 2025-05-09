#METODOS DE CLASSE ESTÃO LIGADOS A CLASSE E NAO AO OBJETO -> RECEBE UM PRIMEIRO PARAMETRO QUE APONTA PARA CLASSE -> METODOS DE FABRICA
#METODO ESTATICO NÃO TEM REFERENCIA PARA FAZER MODIFICACOES (RECEBEM APENAS VALORES) -> FUNCOES UTILITARIAS

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def calc_data_nascimento(self, ano, mes, dia, nome):
        idade = 2025 - ano
        return self(nome, idade)

    @staticmethod
    def eh_maior(idade):
        return idade >= 18


p = Pessoa("Guilherme", 28)
print(p.nome, p.idade)

p2 = Pessoa.calc_data_nascimento(2003, 5, 25, "Mateus")
print(p2.nome, p2.idade)
print(Pessoa.eh_maior(p2.idade))
print(Pessoa.eh_maior(p.idade))