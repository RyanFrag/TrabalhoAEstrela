from typing import List, Tuple, Optional

def build_path(state):
    path = []
    while state:
        path.append(state.tabuleiro)
        state = state.pai
    return path

def expandir_fila(fila_prioridade, estado, visitados, heuristica, estado_objetivo):
    for filho in estado.gerar_filhos(estado_objetivo, heuristica):
        if filho.tabuleiro not in visitados:
            custo_total= estado.custo + 1
            custo = custo_total + heuristica.calcular_heuristica(heuristica, filho.tabuleiro, estado_objetivo.tabuleiro)
            fila_prioridade.append((custo, filho))
    fila_prioridade.sort(key=lambda x: x[0])


def resolver(heuristic, initial_board, goal_board) -> Tuple[Optional[List[int]], int]:
    initial_state = heuristic(initial_board, None, None)
    goal_state = heuristic(goal_board, None, None)
    priority_queue = [(0, initial_state)]
    visited = []
    while priority_queue:
        _, state = priority_queue.pop(0)
        if state.visitado:
            continue
        state.visited = True
        visited.append(state.tabuleiro)
        if state.tabuleiro == goal_state.tabuleiro:
            caminho = build_path(state)
            custo = len(caminho) - 1
            return caminho, custo
        expandir_fila(priority_queue, state, visited, heuristic, goal_state)
    return None, 0