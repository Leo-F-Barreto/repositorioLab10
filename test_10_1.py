from Ex_10_1 import GerenciadorDeVendas

import pytest
from unittest.mock import patch, mock_open

@pytest.fixture
def gerenciador():
    return GerenciadorDeVendas()


@pytest.fixture
def itens_teste():
    return [
        {'preco': 100.0, 'quantidade': 2},  # 200.0
        {'preco': 50.0, 'quantidade': 1}  # 50.0 -> Total = 250.0
    ]


@pytest.fixture
def cliente_normal():
    return {'nome': 'João Silva', 'tipo': 'NORMAL'}


@pytest.fixture
def cliente_vip():
    return {'nome': 'Maria Souza', 'tipo': 'VIP'}


def test_venda_cliente_normal_cartao(gerenciador, itens_teste, cliente_normal, capsys):
    # Usa o mock_open para evitar a criação de um arquivo real durante o teste
    with patch("builtins.open", mock_open()) as mock_file:
        gerenciador.processar_venda_e_gerar_relatorio(itens_teste, cliente_normal, 'CARTAO')

        # Verifica as saídas impressas no console (stdout)
        captured = capsys.readouterr()
        assert "Cobrando R$ 250.0 no cartão de crédito..." in captured.out
        assert "Venda processada com sucesso." in captured.out

        # Verifica se o arquivo foi aberto corretamente e se o conteúdo gravado está exato
        mock_file.assert_called_once_with("relatorio_vendas.txt", "a")
        handle = mock_file()
        relatorio_esperado = "--- Relatório de Venda ---\nCliente: João Silva\nTotal: R$ 250.0\n"
        handle.write.assert_called_once_with(relatorio_esperado)


def test_venda_cliente_vip_boleto(gerenciador, itens_teste, cliente_vip, capsys):
    with patch("builtins.open", mock_open()) as mock_file:
        gerenciador.processar_venda_e_gerar_relatorio(itens_teste, cliente_vip, 'BOLETO')

        # O total deve ter 10% de desconto (250.0 * 0.90 = 225.0)
        captured = capsys.readouterr()
        assert "Gerando boleto no valor de R$ 225.0..." in captured.out

        handle = mock_file()
        relatorio_esperado = "--- Relatório de Venda ---\nCliente: Maria Souza\nTotal: R$ 225.0\n"
        handle.write.assert_called_once_with(relatorio_esperado)


