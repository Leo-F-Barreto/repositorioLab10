class ProcessadorFinanceiro:
    def processar_pagamento_credito(self, valor):
        if valor > 0:
            valor_com_taxa = valor + (valor * 0.05)
            print(f"Processando crédito: R$ {valor_com_taxa}")
        else:
            print("Valor inválido")

    def processar_pagamento_debito(self, valor):
        if valor > 0:
            valor_com_taxa = valor + (valor * 0.02)
            print(f"Processando débito: R$ {valor_com_taxa}")
        else:
            print("Valor inválido")
