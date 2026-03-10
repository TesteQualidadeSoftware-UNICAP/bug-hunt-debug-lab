"""
MAIN DO LABORATÓRIO DE DEBUG

Este arquivo funciona como ponto de entrada do sistema.

Objetivo:
Permitir que os alunos executem diferentes módulos do projeto
que contêm bugs intencionais para investigação.

Durante a atividade os alunos devem:
1. Executar o programa
2. Escolher um módulo
3. Observar o comportamento
4. Aplicar técnicas de debug
5. Registrar o bug encontrado
"""

from desconto import calcular_desconto
from media import calcular_media
from login import login
from carrinho import calcular_total
from divisao import dividir
from fatorial import fatorial
from fantasma import processar_pedido


def menu():

    print("\n===== LABORATÓRIO DE DEBUG =====\n")

    print("1 - Testar cálculo de desconto")
    print("2 - Testar cálculo de média")
    print("3 - Testar login")
    print("4 - Testar carrinho de compras")
    print("5 - Testar divisão")
    print("6 - Testar fatorial")
    print("7 - Testar BUG FANTASMA")
    print("0 - Sair")


def executar_opcao(opcao):

    # Técnica de Debug sugerida:
    # observar o comportamento do sistema antes de investigar o código

    if opcao == "1":

        print("\n--- Teste Desconto ---")

        preco = 100
        percentual = 10

        # Técnica de debug: verificar valores de entrada
        print("[DEBUG] preco:", preco)
        print("[DEBUG] percentual:", percentual)

        resultado = calcular_desconto(preco, percentual)

        print("Resultado:", resultado)

    elif opcao == "2":

        print("\n--- Teste Média ---")

        notas = [8, 7, 9, 6]

        print("[DEBUG] notas:", notas)

        resultado = calcular_media(notas)

        print("Média:", resultado)

    elif opcao == "3":

        print("\n--- Teste Login ---")

        usuario = "admin"
        senha = "1234"

        print("[DEBUG] usuario:", usuario)
        print("[DEBUG] senha:", senha)

        resultado = login(usuario, senha)

        print("Resultado:", resultado)

    elif opcao == "4":

        print("\n--- Teste Carrinho ---")

        itens = [
            {"preco": 50, "quantidade": 2},
            {"preco": 30, "quantidade": 1}
        ]

        print("[DEBUG] itens:", itens)

        total = calcular_total(itens)

        print("Total:", total)

    elif opcao == "5":

        print("\n--- Teste Divisão ---")

        # Técnica de debug: observar parâmetros antes da operação
        a = 10
        b = 0

        print("[DEBUG] a:", a)
        print("[DEBUG] b:", b)

        print(dividir(a, b))

    elif opcao == "6":

        print("\n--- Teste Fatorial ---")

        numero = 5

        print("[DEBUG] numero:", numero)

        print(fatorial(numero))

    elif opcao == "7":

        print("\n--- Teste BUG FANTASMA ---")

        valor = 100

        # Esse bug só aparece após algumas execuções
        # Técnica de debug recomendada:
        # executar várias vezes e observar o comportamento

        print("[DEBUG] valor inicial:", valor)

        resultado = processar_pedido(valor)

        print("Valor final:", resultado)

    elif opcao == "0":

        print("\nEncerrando programa...")

    else:

        print("\nOpção inválida.")


def main():

    opcao = ""

    # Loop principal do programa
    while opcao != "0":

        menu()

        opcao = input("\nEscolha uma opção: ")

        # Técnica de debug:
        # pode-se colocar um breakpoint aqui para investigar o fluxo
        # breakpoint()

        executar_opcao(opcao)


# Ponto de entrada da aplicação
if __name__ == "__main__":

    main()
