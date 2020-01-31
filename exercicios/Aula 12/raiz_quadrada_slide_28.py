#Slide 28 da aula 12
#Método de Newton
#f(x)=x²-y
#x(1)=y/2
#x(n+1)=x(n)-f(x(n))/f'(x(n))

def funcao(x,y):
    f=x*x-y
    return f

def derivada(x):
    d=2*x
    return d

y=float(input('Quero calcular raiz de: '))
if y<0:
    print('Não sei complexos ainda')
else:
    x=y/2
    aprox=1
    while aprox<=20:
        f=funcao(x,y)
        d=derivada(x)
        x=x-f/d
        aprox=aprox+1
    print(x)
