'''
Nome: Anne Feng Cai;RA:261026
Descrição: Programa para calcular ações de 4 empresas
Entradas: d, valores de ações de empresa 1-4 em d dias
Saídas: ação de empresa X, compra, venda, lucro; lucro total
'''
#função para listar dias de compra e venda e lucro obtido
def lucro(empX,d,empXc,empXv,empXl):
    for i in range(d):
        for j in range(i,d):
            if empX[j] > empX[i]:
                empXc.append(i)
                empXv.append(j)
                empXl.append((empX[j]-empX[i]))
    empXc.append(0)
    empXv.append(0)
    empXl.append(0)
    return empXc, empXv, empXl
#função para calcular as possibilidades de ações com 4 empresas
def lucrototal(ac,av,al,bc,bv,bl,cc,cv,cl,dc,dv,dl):
    luctot=0
    dados=0
    for i in range(len(av)):
        for j in range(len(bv)):
            if bc[j] < av[i]:
                continue
            for k in range (len(cv)):
                if cc[k] < bv[j]:
                    continue
                for l in range (len(dv)):
                    if dc[l] < cv[k]:
                        continue
                    if (luctot <= al[i]+bl[j]+cl[k]+dl[l]):
                        luctot = al[i]+bl[j]+cl[k]+dl[l]
                        dados=[i,j,k,l,luctot]
    return dados
#função para permutar a ordem de compra das 4 empresas
def permutacao(lista):
    ordemp=[]
    dadosemp=[]
    for a in range(1,13,3):
        for b in range(1,13,3):
            if b!=a:
                for c in range(1,13,3):
                    if c!=b and c!=a:
                        for d in range(1,13,3):
                            if d!=c and d!=b and d!=a:
                                parametros=[a,b,c,d]
                                ordemp.append(parametros)
                                dado=lucrototal(lista[a],lista[a+1],lista[a+2],lista[b],lista[b+1],lista[b+2],lista[c],lista[c+1],lista[c+2],lista[d],lista[d+1],lista[d+2])
                                dadosemp.append(dado)
    return ordemp, dadosemp
#inputando os dados brutamente
emp1=[]; emp2=[]; emp3=[]; emp4=[]
d=int(input()) #dias de acoes
for i in range(d):
    emp1.append(float(input()))
for i in range(d):
    emp2.append(float(input()))
for i in range(d):
    emp3.append(float(input()))
for i in range(d):
    emp4.append(float(input()))
#calculando possibilidades de compra e venda e lucro obtido
emp1c=[]; emp1v=[]; emp1l=[]
emp2c=[]; emp2v=[]; emp2l=[]
emp3c=[]; emp3v=[]; emp3l=[]
emp4c=[]; emp4v=[]; emp4l=[]
(emp1c, emp1v, emp1l) = lucro(emp1, d, emp1c, emp1v, emp1l)
(emp2c, emp2v, emp2l) = lucro(emp2, d, emp2c, emp2v, emp2l)
(emp3c, emp3v, emp3l) = lucro(emp3, d, emp3c, emp3v, emp3l)
(emp4c, emp4v, emp4l) = lucro(emp4, d, emp4c, emp4v, emp4l)

lista=[[],emp1c,emp1v,emp1l,emp2c,emp2v,emp2l,emp3c,emp3v,emp3l,emp4c,emp4v,emp4l]
(ordem, dad) = permutacao(lista) #lista ordem para armazenar a ordem de compra e lista dad para armazenar os índices dos dias de compra
maior=0 #procurando maior lucro
imax=0
for i in range(24):
    if dad[i][4]>maior:
        maior=dad[i][4]
        imax=i
for j in range(3,-1,-1): #organizando as informações para printar
    x=ordem[imax][j]
    indice=dad[imax][j]
    if x==1:
        indice1=indice
    if x==4:
        indice2=indice
    if x==7:
        indice3=indice
    if x==10:
        indice4=indice
if lista[3][indice1]!=0:
    print('acao %d: compra %d, venda %d, lucro %.2f' %(1, (lista[1][indice1]+1), (lista[2][indice1]+1), lista[3][indice1]))
if lista[6][indice2]!=0:
    print('acao %d: compra %d, venda %d, lucro %.2f' %(2, (lista[4][indice2]+1), (lista[5][indice2]+1), lista[6][indice2]))
if lista[9][indice3]!=0:
    print('acao %d: compra %d, venda %d, lucro %.2f' %(3, (lista[7][indice3]+1), (lista[8][indice3]+1), lista[9][indice3]))
if lista[12][indice4]!=0:
    print('acao %d: compra %d, venda %d, lucro %.2f' %(4, (lista[10][indice4]+1), (lista[11][indice4]+1), lista[12][indice4]))
print('Lucro: %.2f' %dad[imax][4])
