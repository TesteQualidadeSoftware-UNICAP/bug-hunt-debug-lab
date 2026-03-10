def calcular_media(notas):

    total = 0

    for nota in notas:
        total += nota

    # BUG
    media = total / (len(notas) - 1)

    return media


if __name__ == "__main__":

    notas = [8,7,9,6]

    print("Média:", calcular_media(notas))
