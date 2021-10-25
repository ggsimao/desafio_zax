from model import Moto, Loja
import control
import sys

if __name__ == "__main__":
    assert len(sys.argv) <= 2

    motos = []
    motos.append(Moto(1, 2, [1, 2, 3]))
    motos.append(Moto(2, 2, [1, 2, 3]))
    motos.append(Moto(3, 2, [1, 2, 3]))
    motos.append(Moto(4, 2, [1]))
    motos.append(Moto(5, 3, [1, 2, 3]))

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        assert arg.isdigit()
        assert 0 < int(arg) <= 5
        motos_a_consultar = [motos[int(arg) - 1]]
    else:
        motos_a_consultar = motos

    lojas = []
    lojas.append(Loja(1, [50, 50, 50], 0.05))
    lojas.append(Loja(2, [50, 50, 50, 50], 0.05))
    lojas.append(Loja(3, [50, 50, 100], 0.15))

    pedidos = control.atribuir_entregas(motos, lojas)

    control.infos(motos_a_consultar, pedidos)
