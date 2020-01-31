#Slide 22 da Aula 07

#Números primos
#observação: este programa só analisa o conjunto dos números naturais

n=int(input('Quero ver se é primo: '))
indicadora=True
if n==0:
    print('Não está definido')
elif n==1:
    print('Pode ou não ser, depende da definição usada para números primos')
else:
    i=2
    while (i<=(n**(1/2))) and indicadora:
        if (n%i==0):
            indicadora=False
        i=i+1
    if indicadora==False:
        print(str(n)+' não é primo')
    else:
        print(str(n)+' é primo')
