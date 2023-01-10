class JogoDaVelha:
    def __init__(self):
        self.matriz = [['', '', ''], ['', '', ''], ['', '', '']]
        self.vez = 'X'
        self.fim_de_jogo = False

    def jogada(self, linha, coluna):
        if self.matriz[linha][coluna] != '':
            return False
        if self.fim_de_jogo:
            return False

        self.matriz[linha][coluna] = self.vez
        vencedor = self.vencedor()
        if vencedor is not None:
            self.fim_de_jogo = True
            return vencedor

        if self.vez == 'X':
            self.vez = 'O'
        else:
            self.vez = 'X'

        return True

    def vencedor(self):
        # Verifica as linhas
        for linha in self.matriz:
            if linha[0] == linha[1] == linha[2] and linha[0] != '':
                return linha[0]

        # Verifica as colunas
        for i in range(3):
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] and self.matriz[0][i] != '':
                return self.matriz[0][i]

        # Verifica as diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] and self.matriz[0][0] != '':
            return self.matriz[0][0]
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] and self.matriz[0][2] != '':
            return self.matriz[0][2]

        # Verifica se o tabuleiro está cheio
        for linha in self.matriz:
            for coluna in linha:
                if coluna == '':
                    return None

        # Se não há um vencedor e o tabuleiro está cheio, o jogo empatou
        return 'Empate'

    def imprimir_tabuleiro(self):
        for linha in self.matriz:
            print(linha)