n=int(input())
divisor=2
soma_divisores=1
while divisor <= (n/2):
    if n%divisor==0:
        soma_divisores = soma_divisores + divisor
        if soma_divisores==n: #essa condição pode ser colocada dentro do if anterior porque...
            print('o número é perfeito')
    divisor=divisor+1
if soma_divisores!=n:
    print('o número não é perfeito')
