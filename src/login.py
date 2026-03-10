import logging

# Técnica de Debug: Logging
# Logs são usados em produção para registrar eventos do sistema
logging.basicConfig(level=logging.DEBUG)

def login(usuario, senha):

    # Registrando dados recebidos
    logging.debug(f"[DEBUG] usuario recebido: {usuario}")
    logging.debug(f"[DEBUG] senha recebida: {senha}")

    if usuario == "admin" and senha == "123":
        logging.info("Login realizado com sucesso")
        return "Login realizado"

    # Log indicando tentativa de login inválida
    logging.warning("Tentativa de login inválida")

    # BUG: mensagem incorreta retornada
    return "Login realizado"
