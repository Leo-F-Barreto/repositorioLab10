class CalculadoraDeFrete:
    def __init__(self):
        self.tabelas = {
            "MOTO": lambda d: d * 2.0,
            "CARRO": lambda d: d * 3.5 + 10.0,
            "CAMINHAO": lambda d: d * 8.0 + 50.0,
            "BICICLETA": lambda d: d * 1.0
        }

    def calcular_frete(self, tipo_transporte, distancia):
        if tipo_transporte not in self.tabelas:
            raise ValueError("Tipo de transporte desconhecido")
        return self.tabelas[tipo_transporte](distancia)

