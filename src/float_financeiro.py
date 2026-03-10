def calcular_total(preco, quantidade):

    total = preco * quantidade

    # BUG financeiro clássico
    return round(total, 2)
