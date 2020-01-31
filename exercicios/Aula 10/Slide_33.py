#Slide 33 da Aula 10

lista=[]
for i in range(10):
    lista.append(int(input('Digite o valor da posição '+str(i)+' da lista: ')))
C=int(input('Digite o valor de C: '))
multC=False
for i in range(10):
    for j in range(i+1,10):
        if lista[i]*lista[j]==C:
            multC=True
            print(lista[i],lista[j])
if not multC:
    print('Não existem tais números')
