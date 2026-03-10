def dividir(a, b):

    # Técnica de Debug: verificar valores antes da operação
    print("[DEBUG] valor de a:", a)
    print("[DEBUG] valor de b:", b)

    # Possível erro se b for zero
    return a / b


# Teste do comportamento
print(dividir(10, 0))
