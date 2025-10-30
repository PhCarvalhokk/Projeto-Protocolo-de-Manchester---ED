# Simulador do Protocolo de Manchester

Este projeto é um simulador simplificado de um sistema de triagem de pacientes baseado no Protocolo de Manchester. Ele foi desenvolvido como parte da Segunda Avaliação da disciplina de Estrutura de Dados da Fatec Rio Claro.

O objetivo do sistema é classificar pacientes por nível de urgência, inseri-los em filas de prioridade e permitir que sejam chamados para atendimento na ordem correta (do mais urgente para o menos urgente).

## Estruturas de Dados Utilizadas

O projeto é fundamentado em duas estruturas de dados principais:

1.  **Árvore de Decisão (`NodoArvore`)**:
    * Utilizada para realizar a triagem. Cada nó da árvore representa uma pergunta (ex: "O paciente está respirando?").
    * O sistema navega pela árvore com base nas respostas (Sim/Não) até chegar a um nó "folha".
    * As folhas indicam a classificação final de urgência, representada por uma cor.

2. Filas:
    * O sistema mantém cinco filas separadas, uma para cada cor (nível de urgência):
        * Vermelho (emergência)
        * Laranja (muito urgente)
        * Amarelo (urgente)
        * Verde (pouco urgente)
        * Azul (não urgente)
    * Cada fila opera no formato **FIFO (First-In, First-Out)**.

## Funcionalidades

O sistema opera em um loop de menu interativo, permitindo as seguintes operações:

* 1 - Cadastrar paciente
    * Solicita o nome do paciente.
    * Inicia a triagem, fazendo as perguntas da árvore de decisão.
    * Ao final, atribui uma cor e insere o paciente na fila correspondente.

* 2 - Chamar paciente
    * Verifica as filas na ordem de prioridade (Vermelho > Laranja > Amarelo > Verde > Azul).
    * Remove e anuncia o primeiro paciente da fila mais urgente que não esteja vazia.

* 3 - Mostrar status das filas
    * Exibe o tamanho atual (número de pacientes) de cada uma das cinco filas.

* 0 - Sair
    * Encerra a execução do programa.

## Como Executar

1.  Certifique-se de ter o Python 3 instalado.
2.  Salve o código-fonte em um arquivo (ex: `simulador_manchester.py`).
3.  Execute o arquivo através do terminal:

    ```bash
    python simulador_manchester.py
    ```
