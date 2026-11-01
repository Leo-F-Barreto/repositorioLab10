class GerenciadorDeVendas:

    def calcular_subtotal(self, itens):
        subtotal = sum(item['preco'] * item['quantidade'] for item in itens)
        return subtotal

    def calcular_desconto(self, subtotal, cliente):
        if cliente.get('tipo') == 'VIP':
            return subtotal * 0.90
        return subtotal

    def processar_pagamento(self, total_final, metodo_pagamento):
        if metodo_pagamento == 'CARTAO':
            print(f"Cobrando R$ {total_final} no cartão de crédito...")
        elif metodo_pagamento == 'BOLETO':
            print(f"Gerando boleto no valor de R$ {total_final}...")

    def gerar_relatorio(self, nome_cliente, total_final):
        relatorio = f"--- Relatório de Venda ---\nCliente: {nome_cliente}\nTotal: R$ {total_final}\n"
        with open("relatorio_vendas.txt", "a") as f:
            f.write(relatorio)
        print("Venda processada com sucesso.")

    def executar_venda(self, itens, cliente, metodo_pagamento):
        subtotal = self.calcular_subtotal(itens)
        total_final = self.calcular_desconto(subtotal, cliente)

        self.processar_pagamento(total_final, metodo_pagamento)
        self.gerar_relatorio(cliente['nome'], total_final)