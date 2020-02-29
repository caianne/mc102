# Laboratorio 18 - Convolução
# Nome: Anne Feng Cai
# RA: 261026
# Descrição: Programa para alterar uma imagem de entrada com um filtro dado e gerar uma imagem nova
# Escrever na linha de comando: python3.6 lab18.py entrada.pgm matriz-filtro.txt > resultado.pgm

import sys

def mult(mat1,mat2): #função para alterar os pixels de acordo com a matriz filtro
    resultado=0
    for i in range(3):
        for j in range(3):
            resultado=resultado+mat1[i][j]*mat2[i][j]
    return resultado

l1 = []; l2=[]; img=[]; mat=[]; result=[]
# Captando os dados da imagem
imagem = open(sys.argv[1],'r')
while True:
    dado = imagem.readline()
    if (dado==''):
        break
    l1.append(dado)
imagem.close()
# Captando os dados da matriz de mudança
matriz = open(sys.argv[2],'r')
while True:
    dado = matriz.readline()
    if (dado==''):
        break
    l2.append(dado)
matriz.close()

col = int(l1[1].split()[0])
lin = int(l1[1].split()[1])
D = int(l2[0])
# Criando a matriz de imagem original
for i in range(3,len(l1)):
    img.append(l1[i].split())
    for j in range(len(img[i-3])):
        img[i-3][j]=int(img[i-3][j])
# Criando a matriz de filtro
for i in range(1,len(l2)):
    mat.append(l2[i].split())
    for j in range(len(mat[i-1])):
        mat[i-1][j]=int(mat[i-1][j])
# Fazendo a mudança dos pixels da imagem
result.append(img[0])
for i in range(1,lin-1):
    temp=[]
    temp.append(img[i][0])
    for j in range(1,col-1):
        # Pega a matriz 3x3
        mat1=[]
        for a in range(i-1,i+2):
            linha=[]
            for b in range(j-1,j+2):
                linha.append(img[a][b])
            mat1.append(linha)
        c=mult(mat,mat1)//D #chama a função para alterar os pixels
        if c<0:
            c=0
        elif c>255:
            c=255
        temp.append(c)
    temp.append(img[i][j+1])
    result.append(temp)
result.append(img[i+1])
print('P2')
print(col,lin)
print(255)
for i in result:
    for j in i:
        print(j,end=' ')
    print(' ')