#Slide 19 da Aula 07

#Fibonacci

n=(int(input('Quantos números da série de Fibonacci você quer? ')))
print('1, ', end='') #o primeiro 1 não vem de soma nenhuma, a série precisa necessariamente começar no 1
anterior=0 #quem vem antes do 1 será o zero
proximo=1 #o 1 definido anteriormente já entra na variável 'próximo'

for i in range (1,n):
    resultado=anterior+proximo
    anterior=proximo
    proximo=resultado
    if (i==n-1): #para não fazer com que haja um print de uma vírgula a mais no fim
        print(resultado)
    else:
        print(str(resultado)+ ', ',end='')
