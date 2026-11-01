class GerenciadorDeVendas:
    def processar_venda_e_gerar_relatorio(self, itens, cliente, metodo_pagamento):
        # Lógica de cálculo
        total = 0
        for item in itens:
            total += item['preco'] * item['quantidade']

        # Lógica de desconto
        if cliente['tipo'] == 'VIP':
            total = total * 0.90

        # Lógica de pagamento
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total}...")

        # Lógica de relatório
        relatorio = f"--- Relatório de Venda ---\nCliente: {cliente['nome']}\nTotal: R$ {total}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)
        print("Venda processada com sucesso.")