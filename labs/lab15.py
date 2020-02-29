# Nome:Anne Feng Cai; RA:261026
# Descrição: Conjunto de funções para ordenar um campeonato de futebol
# Entrada: Chamada de funções através do arquivo main
# Saída: Mudança de elementos da lista ou impressão da mesma
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
    jogo=jogo.split()
    jogo[1]=int(jogo[1])
    jogo[3]=int(jogo[3])
    saldo=jogo[1]-jogo[3]
    positivo=saldo>0
    for i in range(len(tabela)):
        if tabela[i][0]==jogo[0]:
            tabela[i][3]=tabela[i][3]+saldo
            tabela[i][4]=tabela[i][4]+jogo[1]
            if positivo==True:
                tabela[i][1]=tabela[i][1]+3
                tabela[i][2]=tabela[i][2]+1
            elif saldo==0:
                tabela[i][1]=tabela[i][1]+1
        if tabela[i][0]==jogo[4]:
            tabela[i][3]=tabela[i][3]-saldo
            tabela[i][4]=tabela[i][4]+jogo[3]
            if positivo==False:
                if saldo!=0:
                    tabela[i][1]=tabela[i][1]+3
                    tabela[i][2]=tabela[i][2]+1
                else:
                    tabela[i][1]=tabela[i][1]+1
#*******************************************************************************

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    if time1[1]>time2[1]:
        return 1
    elif time1[1]==time2[1]:
        if time1[2]>time2[2]:
            return 1
        elif time1[2]==time2[2]:
            if time1[3]>time2[3]:
                return 1
            elif time1[3]==time2[3]:
                if time1[4]>time2[4]:
                    return 1
                elif time1[4]==time2[4]:
                    return 0
                else:
                    return -1
            else:
                return -1
        else:
            return -1
    else:
        return -1
#*******************************************************************************

#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    for i in range(len(tabela)-1,0,-1):
        for j in range(i):
            if comparaTimes(tabela[j],tabela[j+1])==1:
                continue
            elif comparaTimes(tabela[j],tabela[j+1])==0:
                continue
            elif comparaTimes(tabela[j],tabela[j+1])==-1:
                tabela[j],tabela[j+1]=tabela[j+1],tabela[j]
#*******************************************************************************

#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for i in range(len(tabela)):
        for j in range(len(tabela[i])-1):
            print(tabela[i][j],end=', ')
        print(tabela[i][j+1])
#*******************************************************************************
