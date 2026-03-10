"""
Arquivo principal do laboratório de Debug.

Este arquivo funciona como o "main" do projeto.
Ele permite executar diferentes exemplos de código
que contêm bugs intencionais para investigação.

Os alunos devem:
1. Executar o programa
2. Escolher um exemplo
3. Identificar o bug
4. Aplicar técnicas de debug
"""

from desconto import calcular_desconto
from media import calcular_media
from login import login
from carrinho import calcular_total
from divisao import dividir
from fatorial import fatorial


def menu():

    print("\n===== LABORATÓRIO DE DEBUG =====\n")

    print("1 - Testar cálculo de desconto")
    print("2 - Testar cálculo de média")
    print("3 - Testar login")
    print("4 - Testar carrinho de compras")
    print("5 - Testar divisão")
    print("6 - Testar fatorial")
    print("0 - Sair")


def executar_opcao(opcao):

    if opcao == "1":

        print("\n--- Teste Desconto ---")

        preco = 100
        percentual = 10

        resultado = calcular_desconto(preco, percentual)

        print("Preço final:", resultado)

    elif opcao == "2":

        print("\n--- Teste Média ---")

        notas = [8, 7, 9, 6]

        resultado = calcular_media(notas)

        print("Média:", resultado)

    elif opcao == "3":

        print("\n--- Teste Login ---")

        usuario = "admin"
        senha = "1234"

        resultado = login(usuario, senha)

        print("Resultado:", resultado)

    elif opcao == "4":

        print("\n--- Teste Carrinho ---")

        itens = [
            {"preco": 50, "quantidade": 2},
            {"preco": 30, "quantidade": 1}
        ]

        total = calcular_total(itens)

        print("Total:", total)

    elif opcao == "5":

        print("\n--- Teste Divisão ---")

        print(dividir(10, 0))

    elif opcao == "6":

        print("\n--- Teste Fatorial ---")

        print(fatorial(5))

    elif opcao == "0":

        print("Encerrando programa.")

    else:

        print("Opção inválida.")


def main():

    opcao = ""

    while opcao != "0":

        menu()

        opcao = input("\nEscolha uma opção: ")

        executar_opcao(opcao)


# Ponto de entrada do programa
if __name__ == "__main__":

    main()
