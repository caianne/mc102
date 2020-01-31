#Slide 33.py

def fatorial(n):
    resultado=1
    for i in range(2,n+1):
        resultado=resultado*i
    return resultado

for n in range(1,21):
    if n<=1:
        print('1, ', end='')
    elif n>1 and n!=20:
        print(str(fatorial(n))+', ', end='')
    elif n==20:
        print(str(fatorial(n)))
