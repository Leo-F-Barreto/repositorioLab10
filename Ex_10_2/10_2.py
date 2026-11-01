from dataclasses import dataclass

@dataclass
class Endereco:
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cep: str

    def __str__(self) -> str:
        return f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - CEP: {self.cep}"


@dataclass
class Contato:
    ddd: str
    telefone_numero: str

    def __str__(self) -> str:
        return f"({self.ddd}) {self.telefone_numero}"


@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: float
    endereco: Endereco
    contato: Contato

    def __str__(self) -> str:
        return (
            f"Funcionario: {self.nome} - {self.cargo}\n"
            f"Contato: {self.contato}\n"
            f"Endereço: {self.endereco}"
        )