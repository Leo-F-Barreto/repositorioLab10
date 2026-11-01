import pytest


# Supondo que a classe Funcionario esteja no mesmo arquivo ou importada.
# from seu_modulo import Funcionario

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


def test_exibir_dados_funcionario(capsys):
    # 1. Preparação (Setup)
    funcionario = Funcionario(
        nome="Ana Silva",
        cargo="Engenheira de Software",
        salario=8500.50,
        rua="Avenida Paulista",
        numero="1000",
        bairro="Bela Vista",
        cidade="São Paulo",
        estado="SP",
        cep="01310-100",
        ddd="11",
        telefone_numero="98765-4321"
    )

    # 2. Ação (Action)
    funcionario.exibir_dados()

    # Captura a saída do print
    captured = capsys.readouterr()

    # 3. Verificação (Assert)
    saida_esperada = (
        "Funcionario: Ana Silva - Engenheira de Software\n"
        "Contato: (11) 98765-4321\n"
        "Endereço: Avenida Paulista, 1000 - Bela Vista, São Paulo/SP - CEP: 01310-100\n"
    )

    assert captured.out == saida_esperada


def test_inicializacao_funcionario():
    funcionario = Funcionario("João", "Analista", 3000, "Rua A", "12", "Centro", "Rio", "RJ", "00000-000", "21",
                              "9999-9999")

    assert funcionario.nome == "João"
    assert funcionario.cargo == "Analista"
    assert funcionario.salario == 3000
    assert funcionario.cep == "00000-000"