class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim plim")
    
    def parar(self):
        print("Parando bicicleta...")
    
    def correr(self):
        print("vrummm....")
    

    #def __str__(self):
    #    return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    def __str__(self):
        return f"{__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
print("=======BICICLETA B1=======")
print(b1)
Bicicleta.buzinar(b1)
b1.correr()
b1.parar()

print(b1.modelo)
print(b1.cor)
print(b1.ano)
print(b1.valor)



b2 = Bicicleta("Verde", "monark", 2000, 189)
print("=======BICICLETA B2=======")
print(b2.modelo)

