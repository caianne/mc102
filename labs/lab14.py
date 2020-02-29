'''
Nome: Anne Feng Cai; RA:261026
Descrição: Um sistema gigante de RA's e operações nela
Entrada: Lista com RA's e comandos de operações finalizando com s
Saída: Respectiva operação ou erro
'''  
def p(li): #impressão da lista
    if li!=[]:
        print(' '.join(li), end='')
        print(' ')
def c(li): #ordenando de forma crescente
    global flag
    flag=1 #indica que foi ordenado de forma crescente
    for i in range(len(li)-1):
        menor=li[i]
        indice=i
        for j in range(i+1,len(li)):
            if li[j]<menor:
                menor=li[j]
                indice=j
        li[i],li[indice]=li[indice], li[i]
def d(li): #ordenando de forma decrescente
    global flag
    flag=2 #indica que foi ordenado de forma decrescente
    for i in range(len(li)-1,-1,-1):
        menor=li[i]
        indice=i
        for j in range(0,i):
            if li[j]<menor:
                menor=li[j]
                indice=j
        li[i],li[indice]=li[indice], li[i]
def b(li,ra): #busca binária de RA
    global flag
    if flag!=0:
        if flag==1: #lista ordenada de forma crescente
            ini=0
            fim=len(li)-1
            while ini<=fim:
                ind=(ini+fim)//2
                print(ind, end=' ')
                if (fim-ini==0 and li[ind]!=ra):
                    break
                elif li[ind]==ra:
                    print('')
                    print(ra,'esta na posicao:',ind)        
                    break
                elif li[ind]>ra:
                    fim=ind-1
                elif li[ind]<ra:
                    ini=ind+1
            se=ra in li
            if se==False:
                print('')
                print(ra,'nao esta na lista!')
        elif flag==2: #lista ordenada de forma decrescente
            ini=0
            fim=len(li)-1
            while ini<=fim:
                ind=(ini+fim)//2
                print(ind, end=' ')
                if (fim-ini==0 and li[ind]!=ra):
                    break
                if li[ind]==ra:
                    print('')
                    print(ra,'esta na posicao:',ind)
                    break
                elif li[ind]<ra:
                    fim=ind-1
                elif li[ind]>ra:
                    ini=ind+1
            se=ra in li
            if se==False:
                print('')
                print(ra,'nao esta na lista!')
    else:
        print('Vetor nao ordenado!')
def i(li,ra): #inserção de RA
    global flag
    if len(li)==150:
        print('Limite de vagas excedido!')
    else:
        se=ra in li #variável para mostrar se o RA já está na lista
        if se==True:
            print('Aluno ja matriculado na turma!')
        else:
            li.append(ra)
            if len(li)>1:
                if flag==1:
                    if int(li[len(li)-2])>int(li[len(li)-1]):
                        aux=li[len(li)-1]
                        li[len(li)-1]=li[len(li)-2]
                        j=len(li)-3
                        while (j>=0 and int(li[j])>int(aux)):
                            li[j+1]=li[j]
                            j=j-1
                        li[j+1]=aux
                elif flag==2:
                    if int(li[len(li)-2])<int(li[len(li)-1]):
                        aux=li[len(li)-1]
                        li[len(li)-1]=li[len(li)-2]
                        j=len(li)-3
                        while (j>=0 and int(li[j])<int(aux)):
                            li[j+1]=li[j]
                            j=j-1
                        li[j+1]=aux   
def r(li,ra): #remoção de RA
    if li==[]:
        print('Nao ha alunos cadastrados na turma!')
    else:
        se=ra in li
        if se==True:
            li.remove(ra)
        else:
            print('Aluno nao matriculado na turma!')
lista=input().split()
linha=input().split()
global flag
flag=0 #indica que a lista começa desordenada
while linha[0]!='s': #s indica saída do programa
    if linha[0]=='p':
        p(lista)
    elif linha[0]=='c':
        c(lista)
    elif linha[0]=='d':
        d(lista)
    elif linha[0]=='b':
        b(lista,linha[1])
    elif linha[0]=='i':
        i(lista,linha[1])
    elif linha[0]=='r':
        r(lista,linha[1])
    linha=input().split()
if linha[0]=='s': #finaliza a execução
    exit()