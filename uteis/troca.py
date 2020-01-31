l=str(input())
l=l.split()
for i in range(3):
    l[i]=float(l[i])
max=l[0]
for i in range(1,3):
    if l[0]<l[i]:
        max=l[i]
        l[0],l[i]=l[i],l[0]
if max>=l[1]+l[2]:
    print('NAO FORMA TRIANGULO')
elif max**2==l[1]**2+l[2]**2:
    print('TRIANGULO RETANGULO')
elif max**2>l[1]**2+l[2]**2:
    print('TRIANGULO OBTUSANGULO')
elif max**2<l[1]**2+l[2]**2:
    print('TRIANGULO ACUTANGULO')
if l[0]==l[1] or l[0]==l[2] or l[1]==l[2]:
    if l[0]==l[1]==l[2]:
        print('TRIANGULO EQUILATERO')
    else:
        print('TRIANGULO ISOSCELES')