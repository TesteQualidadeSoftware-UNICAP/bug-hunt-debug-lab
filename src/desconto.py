def calcular_desconto(preco, percentual):

    desconto = preco * percentual / 100

    # BUG: deveria subtrair
    preco_final = preco + desconto

    return preco_final


if __name__ == "__main__":

    produto = 100
    desconto = 10

    resultado = calcular_desconto(produto, desconto)

    print("Preço final:", resultado)
