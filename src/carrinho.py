def calcular_total(itens):

    total = 0

    # Técnica de Debug: Divisão e Conquista
    # Vamos analisar cada etapa do cálculo separadamente

    for item in itens:

        preco = item["preco"]
        quantidade = item["quantidade"]

        subtotal = preco * quantidade

        # Verificando cada cálculo intermediário
        print("[DEBUG] preco:", preco)
        print("[DEBUG] quantidade:", quantidade)
        print("[DEBUG] subtotal:", subtotal)

        total += subtotal

    print("[DEBUG] total antes do imposto:", total)

    imposto = total * 0.1

    print("[DEBUG] imposto calculado:", imposto)

    # Possível erro na regra de negócio
    return total - imposto
