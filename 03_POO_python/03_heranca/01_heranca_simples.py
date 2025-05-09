class Veiculo:
    def __init__(self, cor, placa, nro_rodas):
        self.cor = cor
        self.placa = placa
        self.nro_rodas = nro_rodas
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, nro_rodas, carregado):
        super().__init__(cor, placa, nro_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "cdf-3r46", 2)
print(moto)
moto.ligar_motor()

carro = Carro("branco", "cfg-3g65", 4)
print(carro)
carro.ligar_motor()

caminhao = Caminhao("roxo", "ddg-3s44", 8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()