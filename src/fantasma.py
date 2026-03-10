"""
BUG FANTASMA

Este bug só aparece quando o módulo é executado várias vezes
ou quando o estado global é reutilizado.

Ele simula um problema comum em sistemas reais:
estado compartilhado entre execuções.
"""

# Estado global do sistema
contador_execucoes = 0


def processar_pedido(valor):

    global contador_execucoes

    contador_execucoes += 1

    print("[DEBUG] contador_execucoes:", contador_execucoes)

    # BUG FANTASMA:
    # A cada terceira execução, o sistema aplica desconto indevido
    if contador_execucoes % 3 == 0:

        print("[DEBUG] BUG FANTASMA ATIVADO")

        return valor * 0.5

    return valor
