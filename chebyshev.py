from tabuleiro import Tabuleiro

class Chebyshev(Tabuleiro):
    def calcular_heuristica(self, tabuleiro, objetivo):
        custo = 0
        for i in range(3):
            for j in range(3):
                valor = tabuleiro[i][j]
                if valor != 0:
                    objetivo_posicao = self.encontrar_posicao(valor, objetivo)
                    custo = max(custo, self.distancia_chebyshev(i, j, objetivo_posicao[0], objetivo_posicao[1]))
        return custo

    @staticmethod
    def encontrar_posicao(valor, objetivo):  
        for i, row in enumerate(objetivo):
            if valor in row:
                return (i, row.index(valor))

    @staticmethod
    def distancia_chebyshev(x1, y1, x2, y2):
        return max(abs(x1 - x2), abs(y1 - y2))
