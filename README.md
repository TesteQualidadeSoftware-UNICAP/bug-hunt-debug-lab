# 🐞 Bug Hunt -- Debug Lab

Repositório utilizado na disciplina **Testes e Qualidade de Software --
UNICAP**.

Este projeto foi criado para praticar **identificação, investigação e
reporte de defeitos (bugs)** utilizando técnicas de debug comuns no
desenvolvimento de software.

------------------------------------------------------------------------

# 🎯 Objetivos de Aprendizagem

Ao final desta atividade, os alunos deverão ser capazes de:

-   Identificar defeitos em código Python
-   Aplicar técnicas de **debug**
-   Investigar a causa raiz de falhas
-   Criar **Bug Reports claros e completos**
-   Classificar defeitos por **severidade**
-   Utilizar **GitHub Issues** para registrar problemas

------------------------------------------------------------------------

# 📁 Estrutura do Projeto

    bug-hunt-debug-lab
    │
    ├── README.md
    │
    ├── src
    │   ├── desconto.py
    │   ├── media.py
    │   ├── login.py
    │   ├── carrinho.py
    │   ├── divisao.py
    │   ├── fatorial.py
    │   ├── float_financeiro.py
    │   ├── mutable_default.py
    │   ├── validacao_email.py
    │   ├── timezone.py
    │   └── api_mock.py
    │
    ├── docs
    │   └── bug_report_template.md
    │
    └── .github
        └── ISSUE_TEMPLATE
            └── bug_report.md

Cada arquivo da pasta **src** contém **um ou mais bugs intencionais**
que devem ser encontrados e reportados.

------------------------------------------------------------------------

# 🐛 Tipos de Bugs Presentes no Projeto

Este laboratório inclui diversos tipos de defeitos encontrados em
sistemas reais:

  Tipo de bug          Exemplo
  -------------------- --------------------------
  Erro lógico          cálculo de desconto
  Erro matemático      média incorreta
  Exceção              divisão por zero
  Estrutura de dados   índice errado
  Validação            email inválido
  Mutabilidade         mutable default argument
  Financeiro           erro de ponto flutuante
  Integração           erro em API
  Timezone             data/hora inconsistente

------------------------------------------------------------------------

# 🧪 Técnicas de Debug Utilizadas

Durante a atividade, os alunos devem aplicar diferentes técnicas de
debug.

## 1️⃣ Print Debugging

Inserir prints no código para observar valores de variáveis.

Exemplo:

    print("[DEBUG] valor:", valor)

------------------------------------------------------------------------

## 2️⃣ Logging

Registrar eventos do sistema usando logs estruturados.

Exemplo:

    import logging
    logging.debug("Valor recebido")

------------------------------------------------------------------------

## 3️⃣ Depuração Interativa (Debugger)

Utilizar breakpoints para pausar a execução e analisar variáveis.

Exemplo:

    breakpoint()

------------------------------------------------------------------------

## 4️⃣ Divisão e Conquista

Isolar partes do código para identificar onde o erro ocorre.

------------------------------------------------------------------------

# 📝 Como Executar o Projeto

Clone o repositório:

    git clone https://github.com/TesteQualidadeSoftware-UNICAP/bug-hunt-debug-lab

Entre no diretório:

    cd bug-hunt-debug-lab

Execute um dos arquivos:

    python src/desconto.py

------------------------------------------------------------------------

# 🐞 Como Reportar um Bug

1.  Identifique o defeito no código
2.  Investigue utilizando técnicas de debug
3.  Acesse a aba **Issues**
4.  Clique em **New Issue**
5.  Utilize o template **Bug Report**
6.  Preencha:

-   descrição do problema
-   passos para reproduzir
-   resultado esperado
-   resultado obtido
-   evidências (logs, prints)
-   severidade

------------------------------------------------------------------------

# 🚦 Classificação de Severidade

  Severidade   Descrição
  ------------ -----------------------------------
  Critical     Sistema inutilizável
  High         Funcionalidade principal afetada
  Medium       Funcionalidade secundária afetada
  Low          Problema menor ou cosmético

------------------------------------------------------------------------

# 🎮 Dinâmica da Atividade

Os alunos trabalharão em **duplas**.

Cada dupla deve:

1.  Executar o código
2.  Identificar bugs
3.  Aplicar técnicas de debug
4.  Criar **Issues detalhadas**
5.  Classificar a severidade do bug

------------------------------------------------------------------------

# 🏆 Pontuação da Atividade

  Ação                   Pontos
  ---------------------- --------
  Bug identificado       2
  Bug report completo    3
  Bug com evidência      2
  Sugestão de correção   3

------------------------------------------------------------------------

# 💡 Desafio Extra

Existe um **bug mais difícil** no projeto.

Quem encontrar primeiro recebe **pontos bônus**.

------------------------------------------------------------------------

# 👩‍🏫 Disciplina

**Testes e Qualidade de Software**\
Bacharelado em Ciência da Computação -- UNICAP

Profª Ivna Valença de Oliveira

------------------------------------------------------------------------

# 📚 Objetivo do Laboratório

Este repositório simula um **ambiente real de investigação de
defeitos**, semelhante ao processo utilizado por equipes de **QA e
Engenharia de Software** na indústria.
