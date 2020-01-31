def selectionsort(lista):
    for i in range(len(lista)-1):
        menor=lista[i]
        indice=i
        for j in range(i,len(lista)):
            if lista[j]<menor:
                menor=lista[j]
                indice=j
        lista[i],lista[indice]=lista[indice], lista[i]
    return lista
def bubblesort(lista):
    for cont in range(1,len(lista)-1):
        for i in range(len(lista)-cont):
            if lista[i]>lista[i+1]:
                lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista
l=[1,2,42,1,45,12,4,2,1,2,4,6,8,5,3]
l=bubblesort(l)
print(l)