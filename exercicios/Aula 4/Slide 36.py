#Está certo?

print('Digite um número:')
a=int(input())
if (a%2==0) and (a<100):
	print('O número é par e menor do que 100')
else:
	if(a>=100):
		print('O número é par e maior ou igual que 100')
if (a%2!=0) and (a<100):
	print('O número é ímpar e menor do que 100')
else:
	if(a>=100):
		print('O número é ímpar e maior ou igual que 100')

#Acho que não, porque ele erra quando o número é ímpar e maior do que 100.

#Update: ainda tem a identação errada de dois conjuntos (if-else)'s. Acaba printando os dois elses para qualquer a>=100.

