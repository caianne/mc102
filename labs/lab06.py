#Nome: Anne Feng Cai; RA: 261026

#Descrição: calcular, comparar e imprimir mensagens sobre a capacidade de um estacionamento
#Entradas: CAP,sequencia
#Saídas: (Seja bem-vindo! Capacidade restante: CAP), quando ainda cabe o veículo que entra; (Veículo muito grande! Capacidade restante: CAP), quando não cabe e (Volte sempre! Capacidade restante: CAP), quando o veículo estiver saindo

CAP=int(input()) #Variável da capacidade, inicialmente é total
veiculo=[] #Lista vazia inicialmente para armazenar a sequência
sequencia=1 #Valor arbitrário, mas diferente de zero, para entrar no looping
while (sequencia!=0):
    sequencia=int(input()) #Entrada dos valores na sequência até que ela seja encerrada (com o zero)
    veiculo.append(sequencia) #Colocando as entradas na lista, incluindo o zero (número de parada)
    if sequencia==0: #Parada do looping com o zero (já definido como o número de parada)
        break
for i in range (0,(len(veiculo)-1)): #(len(veiculo)-1) com -1 porque o último valor na lista é o zero
    if (CAP-veiculo[i]<0): #Caso não caiba, não é possível nem trocar o valor da capacidade (porque fica negativo)
        print('Veiculo muito grande! Capacidade restante: '+str(CAP))
    elif (CAP-veiculo[i]>=0):
        CAP=CAP-veiculo[i] #A fórmula para veículo[i] positivo ou negativo fica sempre igual
        if (veiculo[i]<0):
            print('Volte sempre! Capacidade restante: '+str(CAP))
        elif (veiculo[i]>0):
            print('Seja bem-vindo! Capacidade restante: '+str(CAP))
