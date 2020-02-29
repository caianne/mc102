#Anne Feng Cai; RA:261026
#Descrição: O programa é uma forma de simular o jogo Street Fighter. Serão impressos uma sequência de atualizações de pontos de vida de cada jogar a cada sequência de golpes recebidos (entrada). O jogo será composto de 2 rounds, cada 1 com os jogadores começando com 50 pontos de vida. Perde primeiro quem chega a 0 pontos de vida.
#Entrada: Sequência de números (linha por linha) indicando golpes aplicados (valores positivos) e golpes recebidos (valores negativos).
#Saída: A cada conjunto de golpes, imprime-se o balanço de pontos de vida de quem foi golpeado. Ao fim de dois rounds, imprime-se que Ryu/Ken venceu ou empatou.

golpes=[]
soma_Ryu=0
soma_Ken=0
vida_atual_Ryu=50
vida_atual_Ken=50
indicadora=0
golpes.append(int(input()))

if golpes[len(golpes)-1]<0:
    soma_Ryu=-1*(golpes[len(golpes)-1]) #o sinal que representa soma_Ryu é transformado para positivo
elif golpes[len(golpes)-1]>0:
    soma_Ken=golpes[len(golpes)-1] #o sinal que representa soma_Ken é positivo

while indicadora==0 or indicadora==1 or indicadora==3:
    golpes.append(int(input()))

    if (golpes[len(golpes)-2]*golpes[len(golpes)-1]>=0): #quer dizer que o sinal do último golpe é o mesmo sinal do golpe anterior
        if golpes[len(golpes)-2]<0: #golpe negativo quer dizer que vai para a soma_Ryu porque ele é quem apanha
            soma_Ryu = soma_Ryu - golpes[len(golpes)-1] #menos porque soma_Ryu deve ficar positivo e as entradas de Ryu são negativas
            if (vida_atual_Ryu - soma_Ryu)<=0 and soma_Ryu!=0:
                indicadora=indicadora+1 #indica que Ken ganhou esse round
                print('Ryu: '+str(vida_atual_Ryu)+' - '+str(soma_Ryu)+' = '+str((vida_atual_Ryu)-(soma_Ryu))) #mostra o último balanço de vida do Ryu
                vida_atual_Ryu=50 #recomeça a contagem de pontos de vida
                vida_atual_Ken=50
                soma_Ryu=0
                soma_Ken=0
        else: #golpe positivo (não existe golpe nulo) quer dizer que vai para a soma_Ken porque ele é quem apanha
            soma_Ken = soma_Ken + golpes[len(golpes)-1]
            if (vida_atual_Ken - soma_Ken)<=0 and soma_Ken!=0:
                indicadora=indicadora+3 #indica que Ryu ganhou esse round
                print('Ken: '+str(vida_atual_Ken)+' - '+str(soma_Ken)+' = '+str((vida_atual_Ken)-(soma_Ken))) #mostra o último balanço de vida do Ken
                vida_atual_Ryu=50 #recomeça a contagem de pontos de vida
                vida_atual_Ken=50
                soma_Ryu=0
                soma_Ken=0

    elif (golpes[(len(golpes)-2)]*golpes[(len(golpes)-1)]<0): #quer dizer que os golpes vão precisar ir para somas diferentes
        if golpes[len(golpes)-1]>0: #golpe negativo indo para soma do Ken
            if soma_Ryu!=0:
                print('Ryu: '+str(vida_atual_Ryu)+' - '+str(soma_Ryu)+' = '+str((vida_atual_Ryu)-(soma_Ryu))) #como entra na soma do Ken, quer dizer que o Ryu parou de apanhar e está agredindo o Ken; logo, precisa-se dizer o balanço da agressão que o Ryu levou
                vida_atual_Ryu = vida_atual_Ryu - soma_Ryu
                soma_Ryu=0
            soma_Ken = soma_Ken + golpes[len(golpes)-1]
            if (vida_atual_Ken - soma_Ken)<=0: #se o Ryu revidou o suficiente a ponto de ganhar
                indicadora=indicadora+3 #indica que Ryu ganhou esse round
                print('Ken: '+str(vida_atual_Ken)+' - '+str(soma_Ken)+' = '+str((vida_atual_Ken)-(soma_Ken))) #mostra o último balanço de vida do Ken
                vida_atual_Ryu=50 #recomeça a contagem de pontos de vida
                vida_atual_Ken=50
                soma_Ryu=0
                soma_Ken=0

        elif golpes[len(golpes)-1]<0:
            if soma_Ken!=0:
                print('Ken: '+str(vida_atual_Ken)+' - '+str(soma_Ken)+' = '+str((vida_atual_Ken)-(soma_Ken)))
                vida_atual_Ken = vida_atual_Ken - soma_Ken
                soma_Ken=0
            soma_Ryu = soma_Ryu - golpes[len(golpes)-1]
            if (vida_atual_Ryu - soma_Ryu)<=0:
                indicadora=indicadora+1 #indica que Ken ganhou esse round
                print('Ryu: '+str(vida_atual_Ryu)+' - '+str(soma_Ryu)+' = '+str((vida_atual_Ryu)-(soma_Ryu))) #mostra o último balanço de vida do Ryu
                vida_atual_Ryu=50 #recomeça a contagem de pontos de vida
                vida_atual_Ken=50
                soma_Ryu=0
                soma_Ken=0

if indicadora==2:
    print('Ken venceu')
elif indicadora==4:
    print('empatou')
elif indicadora==6:
    print('Ryu venceu')
