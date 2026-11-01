def criar_reserva(nome_hospede, cpf_hospede, email_hospede, numero_quarto, tipo_quarto, data_checkin, data_checkout, valor_diaria, possui_cafe_da_manha):
    print(f"Reserva criada para {nome_hospede} (CPF: {cpf_hospede})")
    print(f"Quarto {numero_quarto} ({tipo_quarto})")
    print(f"De {data_checkin} até {data_checkout}")
    total_dias = (data_checkout - data_checkin).days
    total = total_dias * valor_diaria
    if possui_cafe_da_manha:
        total += 50 * total_dias
    print(f"Total a pagar: R$ {total}")