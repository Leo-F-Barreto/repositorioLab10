class CalculadoraDeFrete:
    def calcular_frete(self, tipo_transporte, distancia):
        if tipo_transporte == "MOTO":
            return distancia * 2.0
        elif tipo_transporte == "CARRO":
            return distancia * 3.5 + 10.0
        elif tipo_transporte == "CAMINHAO":
            return distancia * 8.0 + 50.0
        elif tipo_transporte == "BICICLETA":
            return distancia * 1.0
        else:
            raise ValueError("Tipo de transporte desconhecido")
