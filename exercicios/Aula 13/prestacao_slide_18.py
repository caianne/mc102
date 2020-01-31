#Slide 18 da aula 13

def prestacao():
    vProd=float(input('Qual o preço do produto? '))
    p=int(input('Quantas prestações? '))
    j=float(input('Qual o valor dos juros em x%? '))
    j=j/100
    pote=pot(j,p)
    vPrest=(pote*vProd*j)/(pote-1)
    print(vPrest)


def pot(j,p):
    pot=(1+j)
    for i in range(p-1):
        pot=(1+j)*pot
    return pot

prestacao()
