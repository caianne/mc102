#Slide 32 da Aula 10

lista=[]
num_media=0
for i in range(10):
    lista.append(float(input('Digite o número da posição '+str(i)+' da lista: ')))
    num_media = num_media + lista[i]
media=num_media/10
print('A média dos números da lista é: '+str(media))
