#Slide 28 da Aula 08

C=int(input('Digite o valor da constante C: '))
for x1 in range(0,C+1):
    for x2 in range(0,C+1-x1):
        for x3 in range(0,C+1-x1-x2):
            x4=C-x1-x2-x3
            print(str(x1)+', '+str(x2)+', '+str(x3)+', '+str(x4))
