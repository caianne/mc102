# Nome: Anne Feng Cai; RA: 261026

# O objetivo do programa é, dados diâmetro (d) e comprimento (h) de um cilindro, calcular o volume do objeto e verificar se o volume é maior ou igual ao volume pedido (em sequência) nos pontos A (a), B (b) e C (c). 
	# Caso o volume seja maior ou igual ao do posto X, sendo X= A,B ou C, emitir ('posto X foi reabastecido') e subtrair o volume em comparação do volume calculado inicialmente. Com o volume subtraído, fazer a comparação com a sequência restante dos pontos e subtraindo conforme possível.
	# Caso contrário, emitir ('posto X nao foi reabastecido') e fazer a comparação com o próximo ponto sem subtrair.

# Entradas:(uma variável por linha) d,h,a,b,c
# Saídas: posto X foi/não foi abastecido; sendo X=A,B ou C

#valores em metros
d=float(input())
h=float(input())

#valores em litros

A=float(input())
B=float(input())
C=float(input())

#valor convertido para litros
vo=3.14*((d/2)**2)*h*1000 

if vo<A:
	print('posto A nao foi reabastecido')
	if vo<B:
		print('posto B nao foi reabastecido')
		if vo<C:
			print('posto C nao foi reabastecido')
		else: #caso em que vo>=C
			print('posto C foi reabastecido')
	else: #caso em que vo>=B
		print('posto B foi reabastecido')
		vo=vo-B #diminuindo do volume reabastecido em B
		if vo<C:
			print('posto C nao foi reabastecido')
		else: #caso em que vo>=C
			print('posto C foi reabastecido')
		
else: #caso em que vo>=A
	print('posto A foi reabastecido')
	vo=vo-A #diminuindo do volume reabastecido em A
	if vo<B:
		print('posto B nao foi reabastecido')
		if vo<C:
			print('posto C nao foi reabastecido')
		else: #caso em que vo>=C
			print('posto C foi reabastecido')
	else: #caso em que vo>=B
		print('posto B foi reabastecido')
		vo=vo-B #diminuindo do volume reabastecido em B
		if vo<C:
			print('posto C nao foi reabastecido')
		else: #caso em que vo>=C
			print('posto C foi reabastecido')
	
