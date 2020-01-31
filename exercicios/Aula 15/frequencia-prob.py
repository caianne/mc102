#Slide 22 da Aula 15
m=int(input('Quantidade de linhas da matriz: '))
n=int(input('Quantidade de colunas da matriz: '))
matriz=[]
for i in range(m):
    linha=[]
    for j in range(n):
        elemento=float(input())
        linha.append(elemento)
    matriz.append(linha)
for l in matriz:
    for e in l:
        print(e, end=' ')
    print()
simp=[matriz[0][0]]
quant=[1]
for l in matriz:
    for e in l:
        for i in range(len(simp)):
            if simp[i]==0:
                quant[i]=quant[i]+1   
        if simp[i]!=e:
                simp.append(e)
                quant.append(1)
maior=[simp[0]]; menor=[simp[0]]; indmai=0; indmen=0
for i in range(len(quant)):
    if quant[i]>indmai:
        del maior[0]
        maior.append(simp[i])
        indmai=i
    if quant[i]<indmen:
        del menor[0]
        menor.append(simp[i])
        indmen=i
for i in range(len(quant)):
    if quant[i]==indmai:
        maior.append(simp[i])
    if quant[i]==indmen:
        menor.append(simp[i])
print(maior)
print(menor)
'''for i in range(len(maior)):
    print(maior(i))'''
'''    print('O elemento com maior frequência, de ', indmai,' vezes, é: ', maior(i))

for i in range(len(menor)):
    print(menor(i))

print('O elemento com menor frequência, de ', indmen,' vezes, é: ', menor(i))
'''