class Tabuleiro:
    def __init__(self, tabuleiro, pai=None, movimento=None):
        self.tabuleiro = tabuleiro  
        self.pai = pai 
        self.movimento = movimento 
        self.visitado = False  
        self.distancia = 0 
        self.custo = 0 

    def calcular_custo(self, custo):
        return self.distancia + custo

    def obter_estado_como_tuple(self):
        return tuple(tuple(row) for row in self.tabuleiro)

    def gerar_filhos(self, objetivo, heuristica):
        filhos = []
        espaco_linha, espaco_coluna = self.encontrar_espaco_vazio()

        movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for movimento in movimentos:
            nova_linha, nova_coluna = espaco_linha + movimento[0], espaco_coluna + movimento[1]

            if self.eh_posicao_valida(nova_linha, nova_coluna):
                novo_tabuleiro = self.criar_copia_tabuleiro()
                self.trocar_pecas(novo_tabuleiro, espaco_linha, espaco_coluna, nova_linha, nova_coluna)
                filho = heuristica(novo_tabuleiro, self, (nova_linha, nova_coluna))
                if objetivo:
                    custo = self.calcular_heuristica(novo_tabuleiro, objetivo.tabuleiro)
                    filho.distancia = custo
                filhos.append(filho)

        return filhos

    def encontrar_espaco_vazio(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 0:
                    return i, j

    def eh_posicao_valida(self, linha, coluna):
        return 0 <= linha < 3 and 0 <= coluna < 3

    def criar_copia_tabuleiro(self):
        return [list(row) for row in self.tabuleiro]

    def trocar_pecas(self, tabuleiro, linha1, coluna1, linha2, coluna2):
        tabuleiro[linha1][coluna1], tabuleiro[linha2][coluna2] = tabuleiro[linha2][coluna2], tabuleiro[linha1][coluna1]


    def calcular_heuristica(self, tabuleiro, objetivo):
        return -1

