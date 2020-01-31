#Slide 20 da Aula 15
mat10x10=[]
for i in range(100):
    linha=[]
    for j in range(100):
        elemento=float(input())
        linha.append(elemento)
    mat10x10.append(linha)
for l in mat10x10:
    for e in l:
        print(e, end=' ')
    print()
naonulo=0
for l in mat10x10:
    for e in l:
        if e!=0:
            naonulo=naonulo+1
print('O número de posições não-nulas é: ', naonulo)
