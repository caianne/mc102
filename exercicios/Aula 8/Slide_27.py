#Slide 27 da Aula 08

#Transformar um decimal num binário, resultando numa saída de uma linha
#Um valor de decimal em binário é: somatório de bi*(2**(i))
n0=int(input('Digite o valor em decimal a ser convertido para binário: '))
n=n0
pot=1 #Começa em 10**0=1
binario_linha=0
while (n!=0):
    b=n%2 #Acha o valor do bi
    binario_linha=binario_linha+pot*b #Faz a soma dos valores binários em decimais
    pot=pot*10
    n=n//2
print('O valor de '+str(n0)+' em binário é: '+str(binario_linha))
