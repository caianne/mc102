#Slide 23 da Aula 09

n=int(input('Vamos fazer algo bem bonito, mas com quantas linhas? '))
linha=1
while linha<=n:
    coluna=1
    while coluna<=n:
        if coluna==linha:
            print('+ ', end='')
        elif coluna!=linha:
            print('* ', end='')
        coluna=coluna+1
    print('')
    linha=linha+1
