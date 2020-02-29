# Laboratorio 19 - Hierarquia
# Nome: Anne Feng Cai
# RA: 261026
# Descrição: Programa que usa recursão para gerar uma saída a partir de uma matriz implementada de forma prática.
# Entrada: linha com n=número de funcionários (3<=n<=30) e k=identificador de funcionário de consulta.
# Saída: Cadeia hierárquica com k no início e o restante em ordem crescente.

import random

def hierarquia(matriz, lista, respo, tam, nada):
    if (lista==nada):
        return None
    else:
        for i in range(tam):
            if lista[i]=='1':
                respo.append(i)
                hierarquia(matriz,matriz[i], respo, tam, nada)

def part(lista,ini,fim):
    pivo=lista[fim]
    while ini<fim:
        while ini<fim and lista[ini] <= pivo:
            ini=ini+1
        while ini<fim and lista[fim] > pivo:
            fim=fim-1
        lista[ini],lista[fim] = lista[fim],lista[ini]
    return ini

def quicksort(lista,ini,fim):
    if ini<fim:
        r=random.randint(ini,fim)
        lista[fim],lista[r] = lista[r], lista[fim]
        posi=part(lista,ini,fim)
        quicksort(lista,ini,posi-1)
        quicksort(lista,posi,fim)

diaghier=[]; resp=[]; zeros=[]
linha=input()
n=int(linha.split()[0])
k=int(linha.split()[1])
# Entrada dos dados nas variáveis de linha temporária (linha), esquema matricial dos funcionários (diaghier) e criação da lista com n 0's (zeros)
for i in range(n):
    linha=input()
    diaghier.append(linha.split())
    zeros.append('0')
# Chamada da função recursiva para armazenar na lista de respostas (resp) a hierarquia correspondente a* funcionári* pedido começando por diaghier[k]
hierarquia(diaghier, diaghier[k], resp, n, zeros)
# Caso * funcionári* k seja a pessoa mais baixa da hierarquia, condição para evitar o IndexError (len(resp)-1) = 0-1 = -1
if len(resp)>0:
    quicksort(resp,0,(len(resp)-1))
    print(k, end=' ')
    for i in range((len(resp)-1)):
        print(resp[i], end=' ')
    print(resp[(len(resp)-1)])
# Printar somente o necessário para a pessoa mais baixa da hierarquia, seu número identificador sem mais nada depois
else:
    print(k)