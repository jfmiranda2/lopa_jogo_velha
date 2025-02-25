#
#Tabuleiro jogo, indicar para o usuario em qual posicao ele deve preecher
#  a | b | c
# --- --- ---
#  d | e | f
# --- --- ---
#  g | h | i

tabuleiro = [
                ['a','b','c'],
                ['d','e','f'],
                ['g','h','i']
            ]
jogadas = 0
vez_jogador = 'X'

#Define uma função -> estrutura necessária para a criação de uma função
def apresentaTabuleiro():
    print(tabuleiro[0])
    print(tabuleiro[1])
    print(tabuleiro[2])

def checkVencedor():
    #Linha
    for linha in range(3):
        concatLinha = tabuleiro[linha][0] + tabuleiro[linha][1] + tabuleiro[linha][2]
        if concatLinha == 'XXX' or concatLinha == 'OOO':
            print('Temos um vencedor!') 
    #Coluna
    for coluna in range(3):
        concatColuna = tabuleiro[0][coluna] + tabuleiro[1][coluna] + tabuleiro[2][coluna]
        if concatColuna == 'XXX' or concatColuna == 'OOO':
            print('Temos um vencedor!') 
    #Diagonal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]   or \
       tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        print('Temos um vencedor!') 

while jogadas < 9:
    print(f'rodada {jogadas}')
    posicao = input('Inserir a posição desejada:')
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == posicao:
                tabuleiro[linha][coluna] = vez_jogador
                jogadas = jogadas + 1 #jogada realizada
                vez_jogador = 'O' if vez_jogador == 'X' else 'X' #altera o jogador  
    
    checkVencedor()
    apresentaTabuleiro()










# for linha in range(3):
#     for coluna in range(3):
#         print(f'tabuleiro[{linha}][{coluna}] = {tabuleiro[linha][coluna]}')
#         # if posicao == tabuleiro[linha][coluna]:
#         #     tabuleiro[linha][coluna] = posicao

# print(tabuleiro)
        
