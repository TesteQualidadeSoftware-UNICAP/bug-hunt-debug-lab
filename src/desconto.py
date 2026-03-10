def calcular_desconto(preco, percentual):

    desconto = preco * percentual / 100

    # BUG
    preco_final = preco + desconto

    return preco_final
