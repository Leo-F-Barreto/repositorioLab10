import pytest
from Ex_10_4 import CalculadoraDeFrete

def test_calcular_frete_moto():
    assert CalculadoraDeFrete().calcular_frete("MOTO", 10) == 20.0

def test_calcular_frete_carro():
    assert CalculadoraDeFrete().calcular_frete("CARRO", 10) == 45.0

def test_calcular_frete_caminhao():
    assert CalculadoraDeFrete().calcular_frete("CAMINHAO", 10) == 130.0

def test_calcular_frete_invalido():
    with pytest.raises(ValueError):
        CalculadoraDeFrete().calcular_frete("AVIAO", 10)
