def calcular_media(notas):

    total = sum(notas)

    # Técnica de Debug: Depuração Interativa
    # breakpoint() pausa a execução do programa
    # permitindo inspecionar variáveis no terminal
    breakpoint()

    # Ao pausar, o aluno pode executar:
    # p total
    # p len(notas)

    media = total / (len(notas) - 1)

    return media
