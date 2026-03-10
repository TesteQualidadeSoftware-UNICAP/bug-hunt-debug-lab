"""
Módulo com exemplo de erro de divisão.

Este arquivo contém um bug intencional (divisão por zero)
que será investigado durante o laboratório de debug.
"""

def dividir(a, b):

    # Técnica de Debug: verificar valores antes da operação
    print("[DEBUG] valor de a:", a)
    print("[DEBUG] valor de b:", b)

    return a / b


# Este bloco só executa quando o arquivo é rodado diretamente
# Não executa quando o módulo é importado pelo main.py
if __name__ == "__main__":

    print(dividir(10, 0))