def selectionSort(vet):
    for i in range(len(vet)-1,0,-1):
        min=indiceMenor(vet,i)
        aux=vet[i]
        vet[i]=vet[min]
        vet[min]=aux

def indiceMenor(vet,inicio):
    min=inicio
    for j in range(inicio,len(vet)):
        if vet[min]>vet[j]:
            min=j
    return min

vet=[5,3,2,1,90,6]
selectionSort(vet)
print(vet)

'''
#outro jeito
def selectionSort(vet):
    for i in range(len(vet)-1):
        max=indiceMaior(vet,i)
        aux=vet[i]
        vet[i]=vet[max]
        vet[max]=aux

def indiceMaior(vet,inicio):
    maior=inicio
    for j in range(inicio,len(vet)):
        if vet[maior]<vet[j]:
            maior=j
    return maior

vet=[5,3,2,1,90,6]
selectionSort(vet)
print(vet)
'''