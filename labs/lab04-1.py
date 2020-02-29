c1=int(input())
c2=int(input())
c3=int(input())
c4=int(input())


if (c1+c2+c3+c4)%2==0: #caso a soma de todas as cargas não seja um valor par, quer dizer que não é possível separar em dois conjuntos cuja soma de cargas deem o mesmo valor
	if (c1+c2)==(c3+c4) or (c1+c3)==(c2+c4) or (c1+c4)==(c2+c3) or (c1+c2+c3)==(c4) or (c1+c2+c4)==(c3) or (c1+c3+c4)==(c2) or (c2+c3+c4)==(c1):
		print('sim')
	else:	
		print('nao')
	
else:
	print('nao')
