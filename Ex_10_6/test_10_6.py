from refatorado_10_6 import ProcessadorFinanceiro

def test_processar_credito(capsys):
    pf = ProcessadorFinanceiro()
    pf.processar_pagamento_credito(100)
    captured = capsys.readouterr()
    assert "Processando crédito: R$ 105.0" in captured.out

def test_processar_debito(capsys):
    pf = ProcessadorFinanceiro()
    pf.processar_pagamento_debito(100)
    captured = capsys.readouterr()
    assert "Processando débito: R$ 102.0" in captured.out

def test_valor_invalido(capsys):
    pf = ProcessadorFinanceiro()
    pf.processar_pagamento_credito(-10)
    captured = capsys.readouterr()
    assert "Valor inválido" in captured.out
