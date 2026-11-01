import pytest
from datetime import date


# Supondo que a função esteja no mesmo arquivo ou importada
def criar_reserva(nome_hospede, cpf_hospede, email_hospede, numero_quarto, tipo_quarto, data_checkin, data_checkout,
                  valor_diaria, possui_cafe_da_manha):
    print(f"Reserva criada para {nome_hospede} (CPF: {cpf_hospede})")
    print(f"Quarto {numero_quarto} ({tipo_quarto})")
    print(f"De {data_checkin} até {data_checkout}")
    total_dias = (data_checkout - data_checkin).days
    total = total_dias * valor_diaria
    if possui_cafe_da_manha:
        total += 50 * total_dias
    print(f"Total a pagar: R$ {total}")


def test_criar_reserva_sem_cafe(capsys):
    checkin = date(2023, 10, 1)
    checkout = date(2023, 10, 5)  # 4 dias de estadia

    criar_reserva("João Silva", "123.456.789-00", "joao@email.com", "101", "Simples", checkin, checkout, 100, False)

    # Captura a saída do console
    captured = capsys.readouterr()

    # Validações
    assert "Reserva criada para João Silva (CPF: 123.456.789-00)" in captured.out
    assert "Quarto 101 (Simples)" in captured.out
    assert "De 2023-10-01 até 2023-10-05" in captured.out
    assert "Total a pagar: R$ 400" in captured.out  # 4 dias * 100


def test_criar_reserva_com_cafe(capsys):
    checkin = date(2023, 11, 10)
    checkout = date(2023, 11, 15)  # 5 dias de estadia

    criar_reserva("Maria Souza", "987.654.321-11", "maria@email.com", "205", "Luxo", checkin, checkout, 200, True)

    captured = capsys.readouterr()

    # Cálculo esperado: (5 * 200) + (5 * 50) = 1000 + 250 = 1250
    assert "Reserva criada para Maria Souza (CPF: 987.654.321-11)" in captured.out
    assert "Total a pagar: R$ 1250" in captured.out