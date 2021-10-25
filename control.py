def lojas_atendidas(moto, loja, no_pedidos):
    assert len(moto.lojas) > 0
    eh_diff = 0
    if len(moto.lojas) > 1 or moto.lojas[0] != loja.id:
        eh_diff = 1
    return moto.id + 5 * eh_diff + 5 * no_pedidos


def atribuir_entregas(motos, lojas):
    pedidos = {}
    for m in motos:
        pedidos[m.id] = []
    fila = []
    for l in lojas:
        diff = len(l.pedidos) - len(fila)
        if diff > 0:
            fila.extend(
                sorted(
                    motos,
                    key=lambda moto: lojas_atendidas(moto, l, len(pedidos[moto.id])),
                )[:diff]
            )
        for p in l.pedidos:
            moto_escolhido = fila.pop(0)
            pedidos[moto_escolhido.id].append((p, l))
    return pedidos


def infos(motos, pedidos):
    for m in motos:
        pedidos_de_m = pedidos[m.id]
        print(str(m) + ":")
        total = 0
        for p in pedidos_de_m:
            loja = p[1]
            total += loja.pagamento * p[0] + m.comissao
            print(p[1])
        print("Ganhou R$" + str(total))
