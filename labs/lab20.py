# Laboratorio 20 - Sudoku

# Funcao: print_sudoku

# A funcao imprime o tabuleiro atual do sudoku de forma animada, isto e,
# imprime o tabuleiro e espera 0.1s antes de fazer outra modificacao.
# Voce deve chamar essa funcao a cada modificacao na matriz resposta, assim
# voce tera uma animacao similar a apresentada no enunciado.
# Essa funcao nao tem efeito na execucao no Susy, logo nao ha necessidade de
# remover as chamadas para submissao.
from lab20_main import print_sudoku
 
  zeroposi = []
  a = 0
  b = 0

def vazio(resposta):

# Funcao: resolve
# Resolve o Sudoku da matriz resposta.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(resposta):
    
    if flag:
        for i in range(9):
            for j in range(9):
                if resposta[i][j]==0: # Captação das posições vazias/nulas
                    coord=(x,y)
                    zeroposi.append(list(coord))
        flag == False

    print_sudoku(resposta)
    return False