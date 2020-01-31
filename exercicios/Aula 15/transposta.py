#Slide 21 da Aula 15
matriz=[]
for i in range(4):
    linha=[]
    for j in range(4):
        elemento=float(input())
        linha.append(elemento)
    matriz.append(linha)
print('A matriz inserida é: ')
for l in matriz:
    for e in l:
        print(e, end=' ')
    print()
transposta=[[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print('A matriz transposta é: ')
for l in transposta:
    for e in l:
        print(e, end=' ')
    print()