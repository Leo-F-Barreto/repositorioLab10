class Pais:
    def __init__(self, nome):
        self.nome = nome

class Estado:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais

class Endereco:
    def __init__(self, rua, estado):
        self.rua = rua
        self.estado = estado

class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor

def verificar_frete_internacional(pedido):
    pais_destino = pedido.cliente.endereco.estado.pais.nome
    if pais_destino != "Brasil":
        print("Sujeito a taxa de importação.")
    else:
        print("Frete nacional padrão.")
