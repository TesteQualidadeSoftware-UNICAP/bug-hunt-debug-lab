def calcular_media(notas):

    total = sum(notas)

    # BUG
    media = total / (len(notas) - 1)

    return media
