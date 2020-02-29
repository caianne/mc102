'''
Nome: Anne Feng Cai; RA:261026
Descrição: O apocalipse de zumbis chegou e a situação se agravou tanto que cientistas agora tentam prever o estado de uma população ao longo dos dias.
Entrada: Uma linha com o número de linhas e colunas de uma matriz. O número de dias de análise. A matriz representativa da população.
Saída: A chamada da iteração e a população em um determinado dia.
'''
def troca(mat): #troca a posicao do meio dependendo das vizinhancas
    if mat[1][1]=='0':
        hum=0
        for j in range(3):
            for i in range(3):
                if mat[i][j]=='1':
                    hum=hum+1
        if hum==2:
            return '1'
        else:
            return '0'
    elif mat[1][1]=='1':
        zumb=0
        for j in range(3):
            for i in range(3):
                if zumb==0:
                    if mat[i][j]=='2':
                        zumb=1
        if zumb!=0:
            return '2'
        else:
            return '1'
    elif mat[1][1]=='2':
        hum=0
        for j in range(3):
            for i in range(3):
                if (hum==0 or hum==1):
                    if mat[i][j]=='1':
                        hum=hum+1
        if hum==2 or hum==0:
            return '0'
        else:
            return '2'

def mat3x3(i,j,lista): #faz com que uma vizinhanca de 9 coisas seja formada
    mat3=[]
    for b in range(j-1,j+2):
        linha=[]
        for a in range(i-1,i+2):
            elemento=lista[a][b]
            linha.append(elemento)
        mat3.append(linha)
    return mat3

txt=str(input())
mn=txt.split()
for i in range(2):
    mn[i]=int(mn[i]) #numero de linhas e colunas
dias=int(input()) #dias analisados
pop=[] #criacao da matriz populacao
for i in range(mn[0]):
    txt=str(input())
    lin=txt.split() 
    pop.append(lin)
print('iteracao 0')
for i in range(mn[0]):
    print(''.join(pop[i]))
nul=['0' for j in range(mn[1]+2)] #fazendo uma linha nula
for i in range(len(pop)):
    pop[i].insert(0,'0')
    pop[i].append('0')
pop.insert(0,nul)
pop.append(nul)

for d in range(1,dias+1):
    popi=[]
    for i in range(1,mn[0]+1):
        l=[]
        for j in range(1,mn[1]+1):
            viz=mat3x3(i,j,pop)
            l.append(troca(viz))
        popi.append(l)
    print('iteracao',d)
    for k in range(mn[0]):
        print(''.join(popi[k]))
    pop=[]
    for e in popi:
        pop.append(e)
    for i in range(len(pop)):
        pop[i].insert(0,'0')
        pop[i].append('0')
    pop.insert(0,nul)
    pop.append(nul)
