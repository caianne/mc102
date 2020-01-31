#Slide 32 da Aula 11

def potencia(a,resultado):
    resultado=resultado*a
    return resultado

for a in range(2,11):
    for b in range (0,11):
        if b==0:
            resultado=1
        else:
            resultado=potencia(a,resultado)
        if a==10 and b==10:
            print(resultado)
        else:
            print(str(resultado)+', ',end='')
