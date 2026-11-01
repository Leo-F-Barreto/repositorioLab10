from dataclasses import dataclass

@dataclass
class Hospede:
    nome: str
    cpf: str
    email: str

@dataclass
class Quarto:
    numero: int
    tipo: str

class Reserva:
    Custo_Cafe_Da_Manha = 50.0

    def __init__(self, hospede: Hospede, quarto: Quarto, data_checkin: date, data_checkout: date,
                 possui_cafe_da_manha: bool = False):
        self.hospede = hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.possui_cafe_da_manha = possui_cafe_da_manha

    @property
    def total_dias(self) -> int:
        return (self.data_checkout - self.data_checkin).days

    def calcular_total(self) -> float:
        total = self.total_dias * self.quarto.valor_diaria
        if self.possui_cafe_da_manha:
            total += self.Custo_Cafe_Da_Manha * self.total_dias
        return total

    def criar_reserva(self) -> str:
        return (
            f"Reserva criada para {self.hospede.nome} (CPF: {self.hospede.cpf})\n"
            f"Quarto {self.quarto.numero} ({self.quarto.tipo})\n"
            f"De {self.data_checkin} até {self.data_checkout}\n"
            f"Total a pagar: R$ {self.calcular_total():.2f}"
        )