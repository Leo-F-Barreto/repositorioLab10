class Pais:
    def __init__(self, nome):
        self.nome = nome

class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
    def get_nome_pais(self):
        return self.pais.nome

class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado
    def get_nome_pais(self):
        return self.estado.get_nome_pais()

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
    def get_nome_pais(self):
        return self.endereco.get_nome_pais()

class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor
    def get_nome_pais_destino(self):
        return self.cliente.get_nome_pais()

def verificar_frete_internacional(pedido):
    pais_destino = pedido.get_nome_pais_destino()
    if pais_destino != "Brasil":
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")
