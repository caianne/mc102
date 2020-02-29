#Nome: Anne Feng Cai; RA: 261026

#Descrição:calcular a soma dos números em 'fluxo_combustivel' para ver se chega em c até t
#Entradas:t,c,fluxo_combustivel
#Saídas:(sim ou nao) + (tempo que a soma chega em c ou o tempo limite t+1)

t=int(input())
c=int(input())
fluxocombustivel=input() #fluxo em string
fluxocombustivel=[int(i) for i in fluxocombustivel.split()] #conversão para lista de inteiros
soma=0
for indice in range(0,len(fluxocombustivel)):
    soma=soma+fluxocombustivel[indice]
    if (soma>=c) or (indice>t): #quando der para acumular c combustível ou quando o tempo t acabar, finalizar programa
        break
if (soma>=c) and (indice<=t):
    print('sim')
    print(indice+1)
else:
    print('nao')
    print(t+1)
