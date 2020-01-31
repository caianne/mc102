#Slide 16 da Aula 07

n=int(input('Quantos números serão lidos? '))

maior_atual=input('Digite o primeiro número: ')
for i in range (1,n):
    comparado=input('Digite o próximo número: ')
    if maior_atual<comparado:
        maior_atual=comparado
print('O maior número digitado dentre os '+str(n)+' números foi: '+str(maior_atual)+'.')
