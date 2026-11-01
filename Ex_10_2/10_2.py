class Funcionario:
    def __init__(self, nome, cargo, salario, rua, numero, bairro, cidade, estado, cep, ddd, telefone_numero):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.ddd = ddd
        self.telefone_numero = telefone_numero

    def exibir_dados(self):
        print(f"Funcionario: {self.nome} - {self.cargo}")
        print(f"Contato: ({self.ddd}) {self.telefone_numero}")
        print(f"Endereço: {self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}")