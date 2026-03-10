def buscar_usuario(usuarios, nome):

    # Técnica de Debug: Caso mínimo de reprodução
    # Testar a função com um conjunto pequeno de dados

    print("[DEBUG] lista de usuarios:", usuarios)
    print("[DEBUG] usuario buscado:", nome)

    for usuario in usuarios:

        print("[DEBUG] verificando:", usuario)

        if usuario == nome:
            return True

    # BUG: deveria retornar False
    return True
