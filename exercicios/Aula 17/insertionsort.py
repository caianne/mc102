#Slide 29 da Aula 17
def insertionsort(lista):
    for i in range(len(lista)-1):
        if lista[i]>lista[i+1]:
            aux=lista[i+1]
            lista[i+1]=lista[i]
            j=i-1
            while (j>=0 and lista[j]>aux):
                lista[j+1]=lista[j]
                j=j-1
            lista[j+1]=aux
    return lista
def insertionsortdec(lista):
    for i in range(len(lista)-1,0,-1):
        if lista[i-1]<lista[i]:
            aux=lista[i-1]
            lista[i-1]=lista[i]
            j=i+1
            while (j<len(lista) and lista[j]>aux):
                lista[j-1]=lista[j]
                j=j+1
            lista[j-1]=aux
    return lista
l=[12,31,2,1,1,4,21,12,3,2,53,1,4,95,22]
l=insertionsortdec(l)
print(l)
