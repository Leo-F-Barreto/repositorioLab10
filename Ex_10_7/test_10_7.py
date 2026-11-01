from Ex_10_7 import Pais, Estado, Endereco, Cliente, Pedido, verificar_frete_internacional

def test_verificar_frete_internacional_brasil(capsys):
    pais = Pais("Brasil")
    estado = Estado("SP", pais)
    endereco = Endereco("Rua A", estado)
    cliente = Cliente("João", endereco)
    pedido = Pedido(cliente, 100)
    
    verificar_frete_internacional(pedido)
    captured = capsys.readouterr()
    assert "Frete nacional padrão." in captured.out

def test_verificar_frete_internacional_exterior(capsys):
    pais = Pais("Argentina")
    estado = Estado("Buenos Aires", pais)
    endereco = Endereco("Rua B", estado)
    cliente = Cliente("Maria", endereco)
    pedido = Pedido(cliente, 200)
    
    verificar_frete_internacional(pedido)
    captured = capsys.readouterr()
    assert "Sujeito a taxa de importação." in captured.out
