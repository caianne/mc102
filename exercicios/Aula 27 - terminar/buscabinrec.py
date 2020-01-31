# Slide 33 da Aula 27
def buscabin(vet,x,ini,fim):
    pos=(fim+ini)//2
    if vet[pos]==x:
        return pos
    elif vet[pos]>x:
        return buscabin(vet,x,ini,pos-1)
    return buscabin(vet,x,pos+1,fim)
l=[0,1,2,3,4,5]
local=buscabin(l,2,0,6)
print(local)
# Slide 34 da Aula 27 - Falta