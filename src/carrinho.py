def calcular_total(itens):

    total = 0

    for item in itens:
        total += item["preco"] * item["quantidade"]

    imposto = total * 0.1

    # BUG
    return total - imposto
