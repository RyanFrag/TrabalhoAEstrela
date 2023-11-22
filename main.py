import time
from manhattan import Manhattan
from NPFL import NPFL
from chebyshev import Chebyshev
from resolve import resolver

def main():
    heuristic_options = {
        1: (Manhattan, "Distância de Manhattan"),
        2: (Chebyshev, "Chebyshev"),
        3: (NPFL, "Número de Peças")
    }
    while True:
        print("Escolha a heurística que você quer usar:")
        for option, (heuristic_class, name) in heuristic_options.items():
            print(f"{option} - {name}")
        choice = int(input("Escolha uma opção: "))
        if choice in heuristic_options:
            heuristic_class, name = heuristic_options[choice]
            initial_board = [[2, 1, 5], [7, 4, 6], [0, 3, 8]]
            goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            start_time = time.time()
            path, cost = resolver(heuristic_class, initial_board, goal_board)
            end_time = time.time()
            if path:
                for step in path:
                    for row in step:
                        print(row)
                cost = len(path) - 1
                print(f"Custo {name}: {cost}")
                print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
            else:
                print("Nenhum caminho encontrado")
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()