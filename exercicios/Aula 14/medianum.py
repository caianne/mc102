#Slide 19 da Aula 14

num=str(input(''))
num=num.replace(',',' ')
num=num.split()
soma=0
for i in num:
    soma=int(i)+soma
media=soma/len(num)
print(media)
