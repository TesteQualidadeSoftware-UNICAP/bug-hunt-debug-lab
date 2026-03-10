def calcular_desconto(preco, percentual):

    # Técnica de Debug: Print Debugging
    # Objetivo: verificar os valores recebidos pela função
    print("[DEBUG] preco recebido:", preco)
    print("[DEBUG] percentual recebido:", percentual)

    desconto = preco * percentual / 100

    # Verificando se o cálculo do desconto está correto
    print("[DEBUG] valor do desconto calculado:", desconto)

    # Possível problema na lógica do cálculo final
    preco_final = preco + desconto

    # Observando o resultado final antes de retornar
    print("[DEBUG] preco_final calculado:", preco_final)

    return preco_final
