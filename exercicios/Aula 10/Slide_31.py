#Slide 31 da Aula 10

lista=[]
maior=0
for i in range(10):
    lista.append(int(input('Digite o valor para a posição '+str(i)+' da lista: ')))
    if lista[i]>maior:
        maior=lista[i]
        indice=i
print('O índice do maior valor da lista é: '+str(indice))
