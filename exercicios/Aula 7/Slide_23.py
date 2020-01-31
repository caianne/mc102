#Slide 23 da Aula 07

print('Vamos determinar se uma sequência de n números está ordenada ou não')
n=int(input('Digite a quantidade de números que você quer analisar: '))
anterior=input('Digite o primeiro número: ')
indicadora=1
while (indicadora<n):
        proximo=input('Digite o próximo número: ')
        if (anterior<=proximo):
            anterior=proximo
            indicadora=indicadora+1
        else:
            break
if (indicadora==n):
    print('A sequência está ordenada')
else:
    print('A sequência não está ordenada')
