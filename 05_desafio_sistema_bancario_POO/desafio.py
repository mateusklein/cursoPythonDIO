from abc import ABC, abstractmethod

NUM_CONTAS = 1
clientes = []

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    def registrar(self, conta):
        operacao = conta.depositar(self.valor)
        
        if(operacao):
            conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"Depósito: {self.valor}"


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        operacao = conta.sacar(self.valor)
        
        if(operacao):
            conta.historico.adicionar_transacao(self)
    

    def __str__(self):
        return f"Saque: {self.valor}"




class Historico:
    def __init__(self, transacoes=None):
        self.transacoes = transacoes if transacoes is not None else []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)



class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
    
    @property
    def saldo(self):
        return self._saldo or 0

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo.")
        else:
            self._saldo = valor

    def sacar(self, valor):
        if(self.limite_saques > 0):
            if(self.saldo >= valor):
                self.saldo -= valor
                print("Saque de R$", valor, " realizado")
                print("Saldo de R$", self.saldo, "limite de R$", self.limite)
                self.limite_saques -= 1
                return True
            if(self.saldo + self.limite  >= valor):
                valor_total = valor
                valor_total -= self.saldo
                self.saldo = 0
                self.limite -= valor_total
                print("Saque de R$", valor, " realizado")
                print("Saldo de R$", self.saldo, "limite de R$", self.limite)
                self.limite_saques -= 1
                return True
            else:
                print("Não foi possível realizar o saque, saldo + limite não suficiente")
                print("Saldo de R$", self.saldo, "limite de R$", self.limite)
                return False
        else:
            print("LIMITE DE SAQUES ATINGIDO, NÃO É POSSÍVEL MAIS SACAR")
            return False
            

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado")
        print("Saldo de R$", conta.saldo, "limite de R$", conta.limite)
        return True

class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def __str__(self):
        return (
            f'{{\n'
            f'    "saldo": "{self.saldo}",\n'
            f'    "numero": "{self.numero}",\n'
            f'    "agencia": "{self.agencia}",\n'
            f'    "historico": "{self.historico}",\n'
            f'    "limite": {self.limite}\n'
            f'    "limite_saques": {self.limite_saques}\n'
            f'}}'
        )



class Cliente:
    def __init__(self, endereco, contas=None):
        self.endereco = endereco
        self.contas = contas if contas is not None else []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        

    def adicionar_conta(self):
        global NUM_CONTAS
        historico = Historico()
        conta = ContaCorrente(saldo=0, numero=NUM_CONTAS, agencia="0001", cliente=self, historico=historico, limite=1000, limite_saques=3)
        NUM_CONTAS+=1
        self.contas.append(conta)
        return conta

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento, contas=None):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return (
            f'{{\n'
            f'    "cpf": "{self.cpf}",\n'
            f'    "nome": "{self.nome}",\n'
            f'    "data_nascimento": "{self.data_nascimento}",\n'
            f'    "endereco": "{self.endereco}",\n'
            f'    "contas": {self.contas}\n'
            f'}}'
        )


def adicionar_cliente():
    cpf = int(input("Digite o cpf do cliente:"))
    nome = input("Digite o nome do cliente:")
    data_nascimento = input("Digite a data de nascimento do cliente:")
    end = input("Digite o endereco do cliente:")

    cliente = PessoaFisica(endereco=end, cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    clientes.append(cliente)
    print(cliente)


def add_conta(cliente):
    if(cliente!=None):
        cliente.adicionar_conta()
    else:
        print("Cliente não existe nos dados do banco")


def realizar_saque(cliente):
    if(cliente.contas == None):
        print("Não tem contas para esse cliente, precisa antes cadastrar para realizar um saque")
    else:
        for conta in cliente.contas:
            print(conta)
        num = int(input("Digite o numero da conta:"))
        conta = busca_contas(cliente.contas, num)
        if(conta == None):
            print("Essa conta nao existe ou não é do seu usuario")
        else:
            valor = float(input("Digite o valor do saque:"))
            saque = Saque(valor)
            cliente.realizar_transacao(conta, saque)



def realizar_deposito(cliente):
    if(cliente.contas == None):
        print("Não tem contas para esse cliente, precisa antes cadastrar para realizar um saque")
    else:
        for conta in cliente.contas:
            print(conta)
        num = int(input("Digite o numero da conta:"))
        conta = busca_contas(cliente.contas, num)
        if(conta == None):
            print("Essa conta nao existe ou não é do seu usuario")
        else:
            valor = float(input("Digite o valor do deposito:"))
            deposito = Deposito(valor)
            cliente.realizar_transacao(conta, deposito)


def exibe_historico(cliente):
    if(cliente.contas == None):
        print("Não tem contas para esse cliente, precisa antes cadastrar para realizar um saque")
    else:
        for conta in cliente.contas:
            print(conta)
        num = int(input("Digite o numero da conta:"))
        conta = busca_contas(cliente.contas, num)
        if(conta == None):
            print("Essa conta nao existe ou não é do seu usuario")
        else:
            hist = conta.historico
            print("====EXTRATO=====")
            for transacao in hist.transacoes:
                print(transacao)
            print("===============")


def busca_contas(contas, num):
    for conta in contas:
        if(conta.numero == num):
            return conta
    return None


def busca_cliente(cpf):
    for cliente in clientes:
        if(cliente.cpf == cpf):
            return cliente
    return None


def menu_banco():
    cpf = int(input("Digite o cpf do cliente:"))
    cliente = busca_cliente(cpf)
    if(cliente != None):
        print("Seja bem-vindo, ", cliente.nome)
        print("==========MENU BANCO==============")
        opcao = 1
        while(opcao!=0):
            print("=================================")
            print("1 - Fazer saque")
            print("2 - Fazer depósito")
            print("3 - Exibir extrato")
            print("4 - Cadastrar nova conta")
            print("0 - Sair")
            print("=================================")
            opcao = int(input("Digite a opcao desejada"))
            match(opcao):
                case 1:
                    print("========SAQUE===========")
                    realizar_saque(cliente)
                    print("=============================")
                case 2:
                    print("========DEPÓSITO===========")
                    realizar_deposito(cliente)
                    print("=============================")
                case 3:
                    print("========EXTRATO===========")
                    exibe_historico(cliente)
                    print("=============================")
                case 4:
                    print("========CADASTRO NOVA CONTA===========")
                    cliente.adicionar_conta()
                    print("=============================")
                case 0:
                    print("=========================")
                    print("========SAINDO===========")
                    print("=========================")
                case _:
                    print("=============================")
                    print("ERRO: Opção não existente")
                    print("=============================")
    else:
        print("ERRO: Cpf não encontrado")


def main_menu():
    opcao = 1
    while(opcao != 0):
        print("=============MENU PRINCIPAL===================")
        print("1 - Cadastrar cliente")
        print("2 - Entrar no banco")
        print("3 - Exibir clientes do banco")
        print("0 - Sair")
        print("=================================")
        opcao = int(input("Digite a opcao desejada"))

        match(opcao):
            case 1:
                print("========CADASTRO CLIENTE===========")
                adicionar_cliente()
                print("=============================")
            case 2:
                print("========ENTRAR NO BANCO===========")
                menu_banco()
                print("=============================")
            case 3:
                print("========EXIBIR CLIENTES===========")
                for cliente in clientes:
                    print(cliente)
                print("=============================")
            case 0:
                print("=============================")
                print("========SAINDO===========")
                print("=============================")
            case _:
                print("=============================")
                print("ERRO: Opção não existente")
                print("=============================")

cliente1 = PessoaFisica(endereco="Av juscelino kubitschek 446", cpf=45321322333, nome="Carlos Cleber", data_nascimento="21/02/2002")
cliente2 = PessoaFisica(endereco="Estrada campo belo 455", cpf=35524352637, nome="Joao Machado", data_nascimento="10/06/2001")
cliente3 = PessoaFisica(endereco="Rua das flores 343", cpf=87326322534, nome="Ana Silva ", data_nascimento="21/02/1997")
add_conta(cliente1)
add_conta(cliente2)
add_conta(cliente3)
clientes.append(cliente1)
clientes.append(cliente2)
clientes.append(cliente3)

cliente = busca_cliente(45321322333)
conta = busca_contas(cliente.contas, 1)

main_menu()
