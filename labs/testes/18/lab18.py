# Laboratorio 18 - Convolução
# Nome: Anne Feng Cai
# RA: 261026
# Descrição: Programa para alterar uma imagem de entrada com um filtro dado e gerar uma imagem nova
# Escrever na linha de comando: python3.6 lab18.py entrada.pgm matriz-filtro.txt > resultado.pgm

import sys

l1 = []; l2=[]; img=[]; mat=[]; result=[]
# Captando os d ados da imagem
imagem = open(sys.argv[1],'r')
while True:
    dado = imagem.readline()
    if (dado==''):
        break
    l1.append(dado)
imagem.close()

col = int(l1[1].split()[0])
lin = int(l1[1].split()[1])
# Criando a matriz de imagem original
for i in range(3,len(l1)):
    img.append(l1[i].split())
    for j in range(len(img[i-3])):
        img[i-3][j]=255-int(img[i-3][j])
print('P2')
print(col,lin)
print(255)
for i in img:
    for j in i:
        print(j,end=' ')
    print(' ')
