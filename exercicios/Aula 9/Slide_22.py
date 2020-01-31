#Slide 22 da Aula 09

n=int(input('Me diga quantas linhas da escada numérica tu queres: '))
linha=1
while linha<=n:
    coluna=0
    numero=1
    while coluna<linha:
        print(str(numero)+' ', end='')
        numero=numero+1
        coluna=coluna+1
    linha=linha+1
    print('')
