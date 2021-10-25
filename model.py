from dataclasses import dataclass


@dataclass(frozen=True)
class Moto:
    id: int
    comissao: int
    lojas: list

    def __repr__(self):
        return "Moto " + str(self.id)


@dataclass(frozen=True)
class Loja:
    id: int
    pedidos: list
    pagamento: float

    def __repr__(self):
        return "Loja " + str(self.id)
