import sys

class Fila:
    """Implementa uma fila básica usando o princípio FIFO (First-In, First-Out)."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Adiciona um item (paciente) ao fim da fila."""
        self.items.append(item)

    def dequeue(self):
        """Remove e retorna o item do início da fila."""
        if not self.is_empty():
            return self.items.pop(0) 
        return None

    def size(self):
        """Retorna o número de itens na fila."""
        return len(self.items)

class NodoArvore:
    """Representa um nó da árvore de decisão.
    
    Pode ser um nó de pergunta (com filhos sim/não)
    ou um nó folha (com a classificação final).
    """
    def __init__(self, pergunta=None, classificacao=None):
        self.pergunta = pergunta
        self.classificacao = classificacao 
        self.filho_sim = None
        self.filho_nao = None

def montar_arvore():
    """Cria e retorna a raiz da árvore de decisão simplificada."""
    
    vermelho = NodoArvore(classificacao=("Vermelho", "emergência (atendimento imediato)"))
    laranja = NodoArvore(classificacao=("Laranja", "muito urgente"))
    amarelo = NodoArvore(classificacao=("Amarelo", "urgente"))
    verde = NodoArvore(classificacao=("Verde", "pouco urgente"))
    
    no_dor_intensa = NodoArvore(pergunta="Está com dor intensa?")
    no_dor_intensa.filho_sim = amarelo
    no_dor_intensa.filho_nao = verde

    no_consciente = NodoArvore(pergunta="Está consciente?")
    no_consciente.filho_sim = no_dor_intensa
    no_consciente.filho_nao = laranja

    raiz = NodoArvore(pergunta="O paciente está respirando?")
    raiz.filho_sim = no_consciente
    raiz.filho_nao = vermelho
    
    return raiz

def triagem(no_atual):
    """Percorre a árvore de decisão fazendo perguntas ao usuário."""
    
    if no_atual.classificacao:
        return no_atual.classificacao

    while True:
        resposta = input(f"{no_atual.pergunta} (s/n): ").strip().lower()
        
        if resposta == 's':
            return triagem(no_atual.filho_sim)
        elif resposta == 'n':
            return triagem(no_atual.filho_nao)
        else:
            print("Resposta inválida. Por favor, digite 's' (sim) ou 'n' (não).")

def main():
    """Loop principal que exibe o menu e gerencia as operações do sistema."""
    
    arvore_de_triagem = montar_arvore()
    
    filas = {
        "Vermelho": Fila(),
        "Laranja": Fila(),
        "Amarelo": Fila(),
        "Verde": Fila(),
        "Azul": Fila()
    }
    
    ordem_prioridade = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]

    while True:
        print("\n=== SISTEMA DE TRIAGEM MANCHESTER ===")
        print("1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            nome = input("Nome do paciente: ")
            
            cor, descricao = triagem(arvore_de_triagem)
            
            filas[cor].enqueue(nome)
            
            print(f"Cor atribuída: {cor} - {descricao}")
            print(f"Paciente {nome} adicionado à fila {cor.lower()}.")

        elif escolha == '2':
            paciente_chamado = False
            for cor in ordem_prioridade:
                if not filas[cor].is_empty():
                    paciente = filas[cor].dequeue()
                    print(f"Chamando paciente da fila {cor.lower()}: {paciente}")
                    paciente_chamado = True
                    break 
            
            if not paciente_chamado:
                print("Nenhum paciente aguardando nas filas.")

        elif escolha == '3':
            print("--- Status das Filas ---")
            for cor in ordem_prioridade:
                print(f"Fila {cor.lower()}: {filas[cor].size()} paciente(s)")
        
        elif escolha == '0':
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()