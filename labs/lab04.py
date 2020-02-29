#Nome: Anne Feng Cai; RA: 261026

#Descrição: Dadas as entradas c1, c2, c3 e c4, que são valores de carga, determinar se é possível ou não separá-las em dois conjuntos (com iguais quantidades de cargas ou não) cujas somas de cada conjunto sejam iguais entre si. Caso seja, a saída é 'sim', caso contrário, 'nao'.
#Entradas: c1, c2, c3, c4
#Saídas: sim ou nao

c1=int(input())
c2=int(input())
c3=int(input())
c4=int(input())

if (c1+c2+c3+c4)%2==0: #caso a soma de todas as cargas não seja um valor par, quer dizer que não é possível separar em dois conjuntos cuja soma de cargas deem o mesmo valor
	carga_separavel = 0 #variável acumuladora, começando no 0. Para cada comparação que não dá igual, é necessário fazer a próxima para garantir a comparação de todas as permutações de somas.
	if carga_separavel==0:#começando a acumular as comparações
		if (c1+c2)==(c3+c4):
			carga_separavel=9 #o 9 é simbólico, e representa simplesmente que a comparação das parcelas de somas em questão deram iguais, garantindo que, pelo menos de uma maneira, é possível separar as cargas de forma igual. Note que o programa só irá fazer as próximas comparações caso carga_separavel seja um valor específico (relativo à comparação anterior que não deu igual)
		else:
			carga_separavel=1	
	#Seguem permutações de somas (com número de termos somados variando também)
	if carga_separavel==1:
		if (c1+c3)==(c2+c4):
			carga_separavel=9
		else:
			carga_separavel=2
	if carga_separavel==2:
		if (c1+c4)==(c2+c3):
			carga_separavel=9
		else:
			carga_separavel=3
	if carga_separavel==3:
		if (c1+c2+c3)==(c4):
			carga_separavel=9
		else:
			carga_separavel=4
	if carga_separavel==4:
		if (c1+c2+c4)==(c3):
			carga_separavel=9
		else:
			carga_separavel=5
	if carga_separavel==5:
		if (c1+c3+c4)==(c2):
			carga_separavel=9
		else:
			carga_separavel=6
	if carga_separavel==6:
		if (c2+c3+c4)==(c1):
			carga_separavel=9
		else:carga_separavel=7

	if carga_separavel==9: #caso em que pelo menos 1 comparação deu igual, o programa também só considera a primeira vez que dá igual, ignorando as próximas comparações
		print('sim')
	if carga_separavel==7: #chega-se em 7 quando todas as comparações foram feitas e de modo nenhum é possível combinar as cargas de forma a terem valores iguais somados
		print('nao')
	
else:
	print('nao')
