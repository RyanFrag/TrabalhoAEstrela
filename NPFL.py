from tabuleiro import Tabuleiro

class NPFL(Tabuleiro):
    def calcular_heuristica(self, tabuleiro, objetivo):
        distancia = 0
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] != objetivo[i][j]:
                    distancia += 1
        return distancia

    