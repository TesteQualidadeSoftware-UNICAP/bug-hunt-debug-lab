def buscar_usuario(usuarios, nome):

    for usuario in usuarios:

        if usuario == nome:
            return True

    # BUG
    return True
