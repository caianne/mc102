def buscabin(vet,x,ini,fim):
    pos=(fim-ini)//2
    if vet[pos]>x:
        buscabin(vet,x,ini,pos-1)
    elif vet[pos]<x:
        buscabin(vet,x,pos+1,fim)
    else:
        return pos
l=[0,1,2,3,4,5]
loca=buscabin(l,2,0,6)