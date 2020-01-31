def buscabin(lista,chave):
    ini=0
    fim=len(lista)-1
    for i in range(ini,fim):
        ind=(ini+fim)//2
        if lista[ind]==chave:
            return ind
        elif lista[ind]>chave:
            fim=ind
        elif lista[ind]<chave:
            ini=ind
    return -1
l=[1,2,5,7,9,11,34,55,77,98,200,467]
print(l)
chav=98
print(chav)
indi=buscabin(l,chav)
print(indi)