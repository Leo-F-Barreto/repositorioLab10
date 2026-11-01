from Ex_10_5 import Produto, ProdutoExporter

def test_calcular_preco_com_imposto():
    p = Produto(1, "Teste", 100.0)
    assert p.calcular_preco_com_imposto() == 115.0

def test_exportar_para_xml():
    p = Produto(1, "Teste", 100.0)
    exporter = ProdutoExporter()
    xml = exporter.exportar_para_xml(p)
    assert xml == "<produto><id>1</id><nome>Teste</nome><preco>100.0</preco></produto>"
