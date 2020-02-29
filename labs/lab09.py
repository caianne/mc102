#Anne Feng Cai; RA:261026
#Descrição: É um programa que imprime uma matriz de forma a mostrar padrão de divisores
#Entradas: Um número entre 1 e 100
#Saídas: Uma matriz com * caso o índice i seja divisor de j ou vice-versa e - caso i e j não sejam divisíveis entre si

n=int(input())
divisores=0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i%j==0 or j%i==0:
            print('*', end='')
            divisores=divisores+1
        else:
            print('-', end='')
    print('\n', end='')
print(divisores)
